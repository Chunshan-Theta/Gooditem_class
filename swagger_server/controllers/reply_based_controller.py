import connexion
import six

from swagger_server.models.comment import Comment  # noqa: E501
from swagger_server.models.message import Message  # noqa: E501
from swagger_server.models.util_mysql import reply_operation as operation


def info_reply_with_array_obj_input(reply_id):  # noqa: E501
    # 拒絕非認證的來源 refuse user or origin
    Origin = connexion.request.headers["Sec-Fetch-Site"] if "Sec-Fetch-Site" in connexion.request.headers else \
    connexion.request.headers["Origin"] if "Origin" in connexion.request.headers else None
    if Origin != "same-site" and Origin != "same-origin" and Origin != "https://goodclass.cf":
        return {"ERROR": "Unauthorized USER"}, 401

    try:
        c = operation()
        return c.select_reply_byid(reply_id=reply_id).to_dict(), 200
    except Exception as e:
        return Message(request_status="error", msg="UNKNOWERROR: {}".format(e)).to_dict(), 200

def delete_reply_with_array_obj_input(reply_id):  # noqa: E501
    # 拒絕非認證的來源 refuse user or origin
    Origin = connexion.request.headers["Sec-Fetch-Site"] if "Sec-Fetch-Site" in connexion.request.headers else \
    connexion.request.headers["Origin"] if "Origin" in connexion.request.headers else None
    if Origin != "same-site" and Origin != "same-origin" and Origin != "https://goodclass.cf":
        return {"ERROR": "Unauthorized USER"}, 401
    try:
        c = operation()

        c.delete_reply_byid(reply_id=reply_id)
        return Message(msg="ok").to_dict(), 200
    except Exception as e:
        return Message(request_status="error", msg="UNKNOWERROR: {}".format(e)).to_dict(), 200


def new_reply_with_array_obj_input(body):  # noqa: E501
    # 拒絕非認證的來源 refuse user or origin
    Origin = connexion.request.headers["Sec-Fetch-Site"] if "Sec-Fetch-Site" in connexion.request.headers else \
    connexion.request.headers["Origin"] if "Origin" in connexion.request.headers else None
    if Origin != "same-site" and Origin != "same-origin" and Origin != "https://goodclass.cf":
        return {"ERROR": "Unauthorized USER"}, 401

    if connexion.request.is_json:
        body_json = connexion.request.get_json()
        body = Comment.from_dict(body_json)  # noqa: E501
        try:
            c = operation()
            comment_id = body_json['comment_id']
            user_memo = body_json['user_memo']

            _ = c.new_reply_byid(comment_id=comment_id,user_memo=user_memo)

            return Message(msg="ok").to_dict(), 200
        except Exception as e:
            return Message(request_status="error", msg="UNKNOWERROR: {}".format(e)).to_dict(), 200
    else:
        error_msg = Message(request_status="error", msg="connexion.request.is_json")
        return error_msg.to_dict(), 500


def update_reply_with_array_obj_input(body):  # noqa: E501
    # 拒絕非認證的來源 refuse user or origin
    Origin = connexion.request.headers["Sec-Fetch-Site"] if "Sec-Fetch-Site" in connexion.request.headers else \
    connexion.request.headers["Origin"] if "Origin" in connexion.request.headers else None
    if Origin != "same-site" and Origin != "same-origin" and Origin != "https://goodclass.cf":
        return {"ERROR": "Unauthorized USER"}, 401

    error_msg = Message(request_status="error", msg="NotImplementedError")
    return error_msg.to_dict(), 500
