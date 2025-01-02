def get_base_prompt(prompt_context, query):
    return f"""
        You are an expert chat assistance that extracts information from the CONTEXT provided between <context> and </context> tags.
        When answering the question contained between <question> and </question> tags be concise and do not hallucinate.
        If you don't have the information just say so.
        Only anwer the question if you can extract it from the CONTEXT provided.

        Do not mention the CONTEXT used in your answer.

        <context>
        {prompt_context}
        </context>
        <question>
        {query}
        </question>
        Answer:
    """