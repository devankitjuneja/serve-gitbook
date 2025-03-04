from fastapi import FastAPI, Query, Path
import requests
import os

app = FastAPI()

GITBOOK_ACCESS_TOKEN = os.getenv('GITBOOK_ACCESS_TOKEN')


@app.get("/v1/spaces/{gitbook_space_id}/content/path/{top_path}")
async def get_gitbook_path(

    gitbook_space_id: str = Path(..., description="GitBook Space ID"),
    top_path: str = Path(..., description="Top path in the GitBook space"),
    format: str = Query("markdown", description="The format of the content")
):

    url = f"https://api.gitbook.com/v1/spaces/{gitbook_space_id}/content/path/{top_path}?format={format}"
    headers = {
        'Authorization': f'Bearer {GITBOOK_ACCESS_TOKEN}'
    }
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return {"error": "Failed to fetch content", "status_code": response.status_code}

    return response.json()


@app.get("/v1/spaces/{gitbook_space_id}/content/page/{page_id}")
async def get_gitbook_page(

    gitbook_space_id: str = Path(..., description="GitBook Space ID"),
    page_id: str = Path(..., description="Page ID in the GitBook space"),
    format: str = Query("markdown", description="The format of the content")
):

    url = f"https://api.gitbook.com/v1/spaces/{gitbook_space_id}/content/page/{page_id}?format={format}"
    headers = {
        'Authorization': f'Bearer {GITBOOK_ACCESS_TOKEN}'
    }
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return {"error": "Failed to fetch content", "status_code": response.status_code}

    return response.json()
