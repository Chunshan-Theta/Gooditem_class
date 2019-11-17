import connexion
import six

from swagger_server.models.comment import Comment  # noqa: E501
from swagger_server.models.message import Message  # noqa: E501
from swagger_server.models.reply import Reply  # noqa: E501
from swagger_server import util
from swagger_server.models.util_mysql import search_operation as operation


def comment_keyword(keyword):  # noqa: E501
    """Info of comments

     # noqa: E501

    :param keyword: split by space
    :type keyword: str

    :rtype: List[Comment]
    """
    return operation().select_comment_byKeyword(keyword=keyword)


def comments_newest():  # noqa: E501
    """Info of comments

     # noqa: E501


    :rtype: List[Comment]
    """
    return operation().select_comment_byNewest()


def replies_newest():  # noqa: E501
    """Info of replies

     # noqa: E501


    :rtype: List[Reply]
    """
    return operation().select_reply_byNewest()

def replies_under_comment(comment_id):
    return operation().select_reply_under_comment(comment_id=comment_id)
