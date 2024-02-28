import rocketlc.space_schedulle_launch as sll
from fastapi import Request
from src.utils.cors_response import response_in_cors
from src.routes.info_rockets.main_route import router


@router.get('/ssl')
async def ssl_info(request:Request):

    data_launch = sll.launchs()
    return response_in_cors(data_launch)