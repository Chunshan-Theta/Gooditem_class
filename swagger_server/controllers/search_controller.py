import connexion
import six

from swagger_server.models.comment import Comment  # noqa: E501
from swagger_server.models.message import Message  # noqa: E501
from swagger_server.models.reply import Reply  # noqa: E501
from swagger_server import util
from swagger_server.models.util_mysql import search_operation as operation
from swagger_server.controllers.util_request import header


def comment_keyword(keyword):  # noqa: E501
    # 拒絕非認證的來源 refuse user or origin
    Origin = connexion.request.headers["Sec-Fetch-Site"] if "Sec-Fetch-Site" in connexion.request.headers else \
    connexion.request.headers["Origin"] if "Origin" in connexion.request.headers else None
    if Origin != "same-site" and Origin != "same-origin" and Origin != "https://goodclass.cf":
        return {"ERROR": "Unauthorized USER"}, 401,header
    """Info of comments

     # noqa: E501

    :param keyword: split by space
    :type keyword: str

    :rtype: List[Comment]
    """

    return operation().select_comment_byKeyword(keyword=keyword),200,header


def comments_newest(start_num = 0):  # noqa: E501
    # 拒絕非認證的來源 refuse user or origin
    Origin = connexion.request.headers["Sec-Fetch-Site"] if "Sec-Fetch-Site" in connexion.request.headers else \
    connexion.request.headers["Origin"] if "Origin" in connexion.request.headers else None
    if Origin != "same-site" and Origin != "same-origin" and Origin != "https://goodclass.cf":
        return {"ERROR": "Unauthorized USER"}, 401,header
    """Info of comments

     # noqa: E501


    :rtype: List[Comment]
    """


    return operation().select_comment_byNewest(start_num),200,header


def replies_newest():  # noqa: E501
    # 拒絕非認證的來源 refuse user or origin
    Origin = connexion.request.headers["Sec-Fetch-Site"] if "Sec-Fetch-Site" in connexion.request.headers else \
    connexion.request.headers["Origin"] if "Origin" in connexion.request.headers else None
    if Origin != "same-site" and Origin != "same-origin" and Origin != "https://goodclass.cf":
        return {"ERROR": "Unauthorized USER"}, 401,header
    """Info of replies

     # noqa: E501


    :rtype: List[Reply]
    """
    return operation().select_reply_byNewest(),200,header

def replies_under_comment(comment_id):
    # 拒絕非認證的來源 refuse user or origin
    Origin = connexion.request.headers["Sec-Fetch-Site"] if "Sec-Fetch-Site" in connexion.request.headers else \
    connexion.request.headers["Origin"] if "Origin" in connexion.request.headers else None
    if Origin != "same-site" and Origin != "same-origin" and Origin != "https://goodclass.cf":
        return {"ERROR": "Unauthorized USER"}, 401,header
    return operation().select_reply_under_comment(comment_id=comment_id),200,header
