from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from crewai import Crew, LLM
from crewai_tools import SerperDevTool
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv
from agents import create_planner, create_writer, create_editor, create_proofreader
from tasks import create_plan_task, create_write_task, create_edit_task, create_proofread_task
import logging

# Load environment variables
load_dotenv()

app = FastAPI()

# Configure CORS for local development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize LLM
llm = LLM(
    model='cerebras/llama-3.3-70b',
    api_key=os.environ.get("CEREBRAS_API_KEY"),
    base_url="https://api.cerebras.ai/v1",
    temperature=0.5,
)

# Initialize search tool
search_tool = SerperDevTool()


# Define request and response models
class TopicRequest(BaseModel):
    topic: str


class BlogResponse(BaseModel):
    blog_post: str


def create_crew(llm, search_tool):
    # Create agents
    planner = create_planner(llm, search_tool)
    writer = create_writer(llm, search_tool)
    editor = create_editor(llm, search_tool)
    proofreader = create_proofreader(llm, search_tool)

    # Create tasks
    plan = create_plan_task(planner, search_tool)
    write = create_write_task(writer, search_tool)
    edit = create_edit_task(editor, search_tool)
    proofreading = create_proofread_task(proofreader, search_tool)

    # Assemble crew
    crew = Crew(
        agents=[planner, writer, editor, proofreader],
        tasks=[plan, write, edit, proofreading],
        verbose=True
    )
    return crew


@app.post("/generate-blog")
async def generate_blog(request: TopicRequest):
    logger.info(f"Received request to generate blog on topic: {request.topic}")
    try:
        crew = create_crew(llm, search_tool)
        logger.info("Crew created successfully")

        result = crew.kickoff(inputs={'topic': request.topic})
        logger.info("Crew execution completed")

        blog_post = result.raw
        if not isinstance(blog_post, str):
            raise ValueError("Blog post output is not a string")

        return BlogResponse(blog_post=blog_post)

    except Exception as e:
        logger.error(f"Error generating blog post: {str(e)}")
        raise HTTPException(
            status_code=500, detail=f"Error generating blog post: {str(e)}")
