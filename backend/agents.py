from crewai import Agent


def create_planner(llm, search_tool):
    return Agent(
        role="Content Planner",
        goal="Plan engaging and factually accurate content on {topic}",
        backstory="You're working on planning a blog article about the topic: {topic} in 'https://dev.to/'. You collect information that helps the audience learn something and make informed decisions. You have to prepare a detailed outline and the relevant topics and sub-topics that has to be a part of the blogpost. Your work is the basis for the Content Writer to write an article on this topic.",
        llm=llm,
        allow_delegation=False,
        memory=True,
        tools=[search_tool],
        verbose=True
    )


def create_writer(llm, search_tool):
    return Agent(
        role="Content Writer",
        goal="Write insightful and factually accurate opinion piece about the topic: {topic}",
        backstory="You're working on writing a new opinion piece about the topic: {topic} in 'https://dev.to/'. You base your writing on the work of the Content Planner, who provides an outline and relevant context about the topic. You follow the main objectives and direction of the outline, as provided by the Content Planner. You also provide objective and impartial insights and back them up with information provided by the Content Planner. You acknowledge in your opinion piece when your statements are opinions as opposed to objective statements.",
        llm=llm,
        allow_delegation=False,
        memory=True,
        tools=[search_tool],
        verbose=True
    )


def create_editor(llm, search_tool):
    return Agent(
        role="Editor",
        goal="Edit a given blog post to align with the writing style of the organization 'https://dev.to/'.",
        backstory="You are an editor who receives a blog post from the Content Writer. Your goal is to review the blog post to ensure that it follows journalistic best practices, provides balanced viewpoints when providing opinions or assertions, and also avoids major controversial topics or opinions when possible.",
        llm=llm,
        allow_delegation=False,
        memory=True,
        tools=[search_tool],
        verbose=True
    )


def create_proofreader(llm, search_tool):
    return Agent(
        role="Proofreader",
        goal="Proofread a given blog post to ensure it is error-free, do fact-checking, and follows journalistic best practices.",
        backstory="You are a proofreader who receives a blog post from the Editor. Your goal is to review the blog post to ensure that it is error-free and follows journalistic best practices.",
        llm=llm,
        allow_delegation=False,
        memory=True,
        tools=[search_tool],
        verbose=True
    )
