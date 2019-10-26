# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.comment import Comment  # noqa: E501
from swagger_server.test import BaseTestCase


class TestCommentBasedController(BaseTestCase):
    """CommentBasedController integration test stubs"""

    def test_info_class_with_array_obj_input(self):
        """Test case for info_class_with_array_obj_input

        Info of class
        """
        query_string = [('comment_id', 56)]
        response = self.client.open(
            '/Chunshan-Theta/goodclass/1.0.0/class',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_new_class_with_array_obj_input(self):
        """Test case for new_class_with_array_obj_input

        Info of class
        """
        body = Comment()
        response = self.client.open(
            '/Chunshan-Theta/goodclass/1.0.0/class',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_class_with_array_obj_input(self):
        """Test case for update_class_with_array_obj_input

        Info of class
        """
        body = Comment()
        response = self.client.open(
            '/Chunshan-Theta/goodclass/1.0.0/class',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
