from mcp.server.fastmcp import FastMCP
from starlette.applications import Starlette
from mcp.server.lowlevel.server import Server as MCPServer
from starlette.requests import Request
from starlette.routing import Route, Mount
import uvicorn
import net
import mcp_config
from pydantic import BaseModel, Field
from typing import Literal, Dict, Any,Optional
import mcp_chain_tool
from mcp_SseServerTransport import Mcp_SseServerTransport,WS_API_KEY

import mcp_logger
logger = mcp_logger.getLogger(__name__)

# 创建 MCP 服务器
mcp = FastMCP("With Sophie MCP Server")


@mcp.tool()
def inspire_chain_of_think_from_thinkpoint(question_or_thinkpoint:str =Field(..., description="The topic or thinkpoint to be explored. Think with Sophie will use this input to search for multiple high-level thought chains that can inspire structured thinking. These chains are provided as options to help the user engage in professional and in-depth reasoning.")
                                           ,optional_arg: Optional[Dict[str, Any]] = None) -> str:
    """This function belongs to the MCP Server “Think with Sophie”, an advanced chain-of-thought tool designed to help users conduct professional and in-depth thinking using high-quality thought chains.
    
    The purpose of this function is to inspire and retrieve the most relevant thought chains from the built-in chain-of-thought repository based on the user’s question or thinkpoint. These candidate chains are intended to serve as structured thinking frameworks for subsequent prompt generation, supporting deeper exploration of the user’s ideas or concerns.
   
    """
    logger.info(f"inspire_chain_of_think_from_thinkpoint reqeust question={question_or_thinkpoint}\n")
    logger.info(f"inspire_chain_of_think_from_thinkpoint reqeust optional_arg={optional_arg}\n")
    urlPath ="train/recommend"
    request_body = {
        "message": question_or_thinkpoint
    }
    header = net.getHeader(optional_arg.get(WS_API_KEY))
    response_data = net.callHttpApi(urlPath,header,request_body)
    recommended_chains= response_data.get('data', [])
    result=[]
    for chain in recommended_chains:
        result.append({
            'chainId':chain.get('trainId'),
            'chainName':chain.get('trainName'),
            'chainDesc':chain.get('trainDesc'),
        })
    result = mcp_config.recommendChainPromptSupper(question_or_thinkpoint,result)
   
    logger.info(f"inspire_chain_of_think_from_thinkpoint response result={result}\n")
    return result

@mcp.tool()
def export_prompt_of_a_chain(export_usage: Literal["chat", "svg", "rdf"] =Field(..., description="""The intended usage of the exported thought chain prompt. Possible values include:
                                                • chat: for use in human-LLM conversations,
                                                • svg: for visual/diagrammatic representation,
                                                • rdf: for structured semantic reasoning via Resource Description Framework."""),
                             name_of_chain:str = Field(..., description="The name or ID of the thought chain whose prompt is to be exported."),
                             optional_arg: Optional[Dict[str, Any]] = None) -> str:
    """This function belongs to the MCP Server “Think with Sophie”, an advanced chain-of-thought tool designed to help users conduct professional and in-depth thinking using high-quality thought chains.
    
    The purpose of this function is to convert a selected high-level thought chain into a structured prompt that can guide a language model in performing professional, methodical, and deep reasoning. Some thought chains may include embedded tool invocation instructions within the prompt to enhance reasoning capabilities or provide essential contextual information.
    
    Please have the exported prompt executed directly by the LLM, ensuring that the results meet the requirements of the thought chain. Note that each advanced thought chain must have an input parameter {ThinkPoint}, which typically corresponds to the question or thinkpoint provided when calling inspire_chain_of_think_from_thinkpoint.
    """
    logger.info(f"findPrompt promptType={export_usage};chainName={name_of_chain}\n")
    logger.info(f"export_prompt_of_a_chain reqeust optional_arg={optional_arg}\n")
  
    chainId = net.getChainIdByName(name_of_chain)
    if chainId is None:
        return f"{name_of_chain} is not exist."
    header = net.getHeader(optional_arg.get(WS_API_KEY))
    typeList =["svg","chat","rdf"]
    if promptType not in typeList:
        promptType ="chat"
    urlPath ="train/export/{promptType}"
    # 请求体
    request_body = {
        "trainId": chainId
    }
    response_data = net.callHttpApi(urlPath,header,request_body)
    result = net.getPromptByType(export_usage,chainId)
    if response_data is not None:
        result = response_data.get("msg")
        result = mcp_config.exportChainPromptSupper(result)
    else:
        result="export failed"
    logger.info(f"export_prompt_of_a_chain response result={result}\n")
    return result

@mcp.tool()
def exec_aux_tool_for_chain(name_of_tool:str =Field(..., description="The name or ID of the auxiliary tool required during the execution of the thought chain."),
                            args_list: Dict[str, Any]=Field(default_factory=dict, description="A list of arguments to be passed to the auxiliary tool. The expected schema for these arguments can be found in the prompt content of the exported thought chain, as generated by export_prompt_of_a_chain.")
                            , optional_arg: Optional[Dict[str, Any]] = None):
    """This function belongs to the MCP Server “Think with Sophie”, an advanced chain-of-thought tool designed to help users conduct professional and in-depth thinking using high-quality thought chains.

The purpose of this function is to execute auxiliary tools referenced by the prompts of certain thought chains. These tools may include knowledge base retrieval, data extraction, information filtering, or custom user-defined utilities. They are designed to work in coordination with prompts, ensuring that complex reasoning tasks have access to the supporting data and context they require to be accurate and complete.

This function supports the invocation of auxiliary tools explicitly mentioned in the prompts of advanced thought chains exported by export_prompt_of_a_chain. In the prompt, such tools must be specified using the format [tool:tool_name].


"""
    logger.info(f"exec_aux_tool_for_chain name_of_tool={name_of_tool}\n")
    logger.info(f"inspire_chain_of_think_from_thinkpoint reqeust optional_arg={optional_arg}\n")
    header = net.getHeader(optional_arg.get(WS_API_KEY))
    return mcp_chain_tool.runChainTool(name_of_tool,args_list)

@mcp.tool()
def search_chains_by_keyword(keyword:str =Field(..., description="Search for Chains based on Chains keyword"),   optional_arg: Optional[Dict[str, Any]] = None):
    """This function belongs to the MCP Server “Think with Sophie”, an advanced chain-of-thought tool designed to help users conduct professional and in-depth thinking using high-quality thought chains.
Search for thinking chains on the Think with Sophie platform using a keyword."""
    logger.info(f"search_chains_by_keyword keyword={keyword}\n")
    logger.info(f"search_chains_by_keyword reqeust optional_arg={optional_arg}\n")
    header = net.getHeader(optional_arg.get(WS_API_KEY))
    data =[]
    return data

@mcp.tool()
def list_my_used_chains(optional_arg: Optional[Dict[str, Any]] = None):
    """This function belongs to the MCP Server “Think with Sophie”, an advanced chain-of-thought tool designed to help users conduct professional and in-depth thinking using high-quality thought chains.
List all the thinking chains I have used before in Think with Sophie."""
    logger.info(f"list_my_used_chains \n")
    logger.info(f"list_my_used_chains reqeust optional_arg={optional_arg}\n")
    header = net.getHeader(optional_arg.get(WS_API_KEY))
    data =[]
    return data

@mcp.tool()
def list_my_favorite_chains(optional_arg: Optional[Dict[str, Any]] = None):
    """This function belongs to the MCP Server “Think with Sophie”, an advanced chain-of-thought tool designed to help users conduct professional and in-depth thinking using high-quality thought chains.
List all my favorite thinking chains in Think with Sophie."""
    logger.info(f"list_my_used_chains \n")
    logger.info(f"list_my_favorite_chains reqeust optional_arg={optional_arg}\n")
    header = net.getHeader(optional_arg.get(WS_API_KEY))
    data =[]
   
    return  data

@mcp.tool()
def list_my_chains(optional_arg: Optional[Dict[str, Any]] = None):
    """This function belongs to the MCP Server “Think with Sophie”, an advanced chain-of-thought tool designed to help users conduct professional and in-depth thinking using high-quality thought chains.
List all the thinking chains I have in Think with Sophie."""
    logger.info(f"list_my_chains \n")
    logger.info(f"list_my_chains reqeust optional_arg={optional_arg}\n")
 
    urlPath ="train/list"
    requestBody={
        "pageNum": "0",
        "pageSize": "200"
    }
    header = net.getHeader(optional_arg.get(WS_API_KEY))
    result = net.callHttpApi(urlPath,header,requestBody)
    # logger.info(f"list_my_chains tmp={result}")
    data = result.get("data")
    if data is not None:
        result = []
        rows = data.get("rows")
        for row in rows:
            result.append({
                "chainId":row.get("id"),
                "chainName":row.get("trainName"),
                "chainDesc":row.get("trainDesc"),
            })
        logger.info(f"list_my_chains result={result}")
        return result
    return "error"
 

# 创建 Starlette 应用
def create_starlette_app(mcp_server: MCPServer, *, debug: bool = False) -> Starlette:
  
    sse = Mcp_SseServerTransport("/messages/")
    

    async def handle_sse(request: Request):
        # 打印所有请求头信息
        print("All request headers:")
        for key, value in request.headers.items():
            print(f"{key}: {value}")

        # 从请求头中获取 API 密钥
        client_api_key = request.headers.get("API-KEY")
        print(f"client_api_key={client_api_key}")
         # 从请求的查询参数中获取 API 
        if client_api_key is None:
           client_api_key = request.query_params.get("apikey")
           print(f"client_api_key={client_api_key}")
        # api_key ="your_api_key_here"
        api_key = "sk-123456"
        # 验证 API 密钥
        if api_key and (client_api_key != api_key):
            from starlette.responses import JSONResponse
            return JSONResponse({"error": "Invalid API Key"}, status_code=401)
 
        async with sse.connect_sse(
                request.scope,
                request.receive,
                request._send,
                api_key,
        ) as (read_stream, write_stream):
            
            await mcp_server.run(
                read_stream,
                write_stream,
                mcp_server.create_initialization_options(),
            )

    return Starlette(
        debug=debug,
        routes=[
            Route("/sse", endpoint=handle_sse),
            Mount("/messages/", app=sse.handle_post_message),
        ],
    )

# 主程序入口
if __name__ == "__main__":
    mcp_server = mcp._mcp_server
    starlette_app = create_starlette_app(mcp_server, debug=True)
    uvicorn.run(starlette_app, host="0.0.0.0", port=8000)
    