from crewai import Task


def create_plan_task(agent, search_tool):
    return Task(
        description=(
            "1. Prioritize the latest trends, key players, and noteworthy news on {topic}.\n"
            "2. Identify the target audience, considering their interests and pain points.\n"
            "3. Develop a detailed content outline including an introduction, key points, and a call to action.\n"
            "4. Include SEO keywords and relevant data or sources."
        ),
        expected_output="A comprehensive content plan document with an outline, audience analysis, SEO keywords, and resources.",
        agent=agent,
        memory=True,
        tools=[search_tool],
    )


def create_write_task(agent, search_tool):
    return Task(
        description=(
            "1. Use the content plan to craft a compelling blog post on {topic}.\n"
            "2. Incorporate SEO keywords naturally.\n"
            "3. Sections/Subtitles are properly named in an engaging manner.\n"
            "4. Ensure the post is structured with an engaging introduction, insightful body, and a summarizing conclusion.\n"
            "5. Proofread for grammatical errors and alignment with the brand's voice.\n"
        ),
        expected_output="A well-written blog post in markdown format, ready for publication, each section should have 2 or 3 paragraphs.",
        agent=agent,
        memory=True,
        tools=[search_tool],
    )


def create_edit_task(agent, search_tool):
    return Task(
        description="Proofread the given blog post for grammatical errors and alignment with the brand's voice.",
        expected_output="A well-written blog post in markdown format, ready for publication, each section should have 2 or 3 paragraphs.",
        agent=agent,
        memory=True,
        tools=[search_tool],
    )


def create_proofread_task(agent, search_tool):
    return Task(
        description="Proofread the given blog post for grammatical errors, fact-checking, and alignment with the brand's voice.",
        expected_output="A well-written blog post in markdown format, ready for publication, each section should have 2 or 3 paragraphs.",
        agent=agent,
        memory=True,
        tools=[search_tool],
    )
