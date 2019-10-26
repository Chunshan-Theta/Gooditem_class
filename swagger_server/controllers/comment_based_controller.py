import connexion
import six

from swagger_server.models.comment import Comment  # noqa: E501
from swagger_server.models.message import Message  # noqa: E501
from swagger_server.models.util_mysql import MysqlObj_pool as mysql


def info_class_with_array_obj_input(comment_id):  # noqa: E501
    """Info of class

     # noqa: E501

    :param comment_id: Eamples: 1
    :type comment_id: int

    :rtype: object
    """
    mysql_connect = mysql()
    result = mysql_connect.exe(sql="SELECT * FROM `comment` WHERE `comment_id` = %s",agrs=[comment_id])[0]

    a = Comment(comment_id=result[0], object_type="normal", class_name=result[1], teacher_name=result[2], user_memo=result[6])

    return a.to_dict(),200


def new_class_with_array_obj_input(body):  # noqa: E501
    """Info of class

     # noqa: E501

    :param body: Pet object that needs to be added to the store
    :type body: dict | bytes

    :rtype: object
    """
    if connexion.request.is_json:
        body = Comment.from_dict(connexion.request.get_json())  # noqa: E501
        return body
    else:
        error_msg = Message(request_status="error", msg="connexion.request.is_json")
        return error_msg.to_dict(),500


def update_class_with_array_obj_input(body):  # noqa: E501
    """Info of class

     # noqa: E501

    :param body: Pet object that needs to be added to the store
    :type body: dict | bytes

    :rtype: object
    """
    if connexion.request.is_json:
        body = Comment.from_dict(connexion.request.get_json())  # noqa: E501
        return body
    else:
        error_msg = Message(request_status="error", msg="connexion.request.is_json")
        return error_msg.to_dict(), 500
