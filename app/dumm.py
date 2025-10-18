# text_to_sql_workflow = TextToSQLWorkflow(
#     obj_retriever = object_retriever,
#     sql_retriever = sql_retriever,
#     sample_retriever=sample_query_retriever,
#     text2sql_prompt = TEXT2SQL_PROMPT,
#     response_synthesis_prompt= RESPONSE_SYNTHESIS_PROMPT,
#     sql_failure_prompt = SQL_FAILURE_PROMPT,
#     llm = llm,
#     verbose = True,
#     timeout = 120
# )

# async def run_workflow(query):
#     handler = await text_to_sql_workflow.run(query = query)
#     return handler
#     # async for event in handler.stream_events():
#     #     if isinstance(event, ProgressEvent):
#     #         print(event, flush = True)

#     # return await handler
# async def execute_workflow():
#     a = await run_workflow("List the products name in descending order, limit 5")
#     return a

# if __name__ == "__main__":
#     result = asyncio.run(execute_workflow())
#     print(result)
#     print(text_to_sql_workflow.memory.get())