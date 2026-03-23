from fastapi import APIRouter, HTTPException, Body
from typing import Dict, Any, List, Optional
from pydantic import BaseModel

from ..pe_module.service import pe_service, engineer_prompt, load_prompt_config, save_prompt_config
from ..pe_module.datarelate_service import pe_datarelate_service

router = APIRouter(
    prefix="/pe",
    tags=["Prompt Engineering"],
    responses={404: {"description": "Not found"}},
)

class RunEngineRequest(BaseModel):
    domain: str
    input_data: Dict[str, Any]
    api_key: Optional[str] = None

class RunEngineResponse(BaseModel):
    results: List[Dict[str, Any]]

class PromptPreviewResponse(BaseModel):
    prompt: str

class PromptConfig(BaseModel):
    header: str
    footer: str

@router.post("/run", response_model=RunEngineResponse)
def run_engine(request: RunEngineRequest):
    """
    Triggers the Prompt Engineering module to generate data based on inputs.
    """
    try:
        print("Data: ", request.input_data)
        data = pe_service.run_engine(
            input_data=request.input_data, 
            domain=request.domain,
            api_key=request.api_key
        )
        
        return {"results": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/datarelate/run", response_model=RunEngineResponse)
def run_datarelate_engine(request: RunEngineRequest):
    """
    Triggers the Prompt Engineering module to generate Data Relate structures via LLM based on node type.
    """
    try:
        print("DataRelate Request: ", request.input_data)
        data = pe_datarelate_service.run_engine(
            input_data=request.input_data, 
            domain=request.domain,
            api_key=request.api_key
        )
        
        return {"results": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/preview", response_model=PromptPreviewResponse)
def get_prompt_preview(request: RunEngineRequest):
    """
    Returns the engineered prompt string that would be sent to the LLM.
    """
    try:
        prompt_str = engineer_prompt(request.input_data, request.domain)
        return {"prompt": prompt_str}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/config", response_model=PromptConfig)
def get_config():
    """
    Returns the current prompt header and footer.
    """
    try:
        config = load_prompt_config()
        return {"header": config.get("header", ""), "footer": config.get("footer", "")}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/config")
def update_config(config: PromptConfig):
    """
    Updates the prompt header and footer.
    """
    try:
        save_prompt_config(config.header, config.footer)
        return {"status": "success"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
