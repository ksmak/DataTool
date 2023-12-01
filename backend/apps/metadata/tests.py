import json
from django.test import TestCase
from django.test import TestCase
from django.contrib.auth import get_user_model

from rest_framework.test import APIClient

from unittest.mock import ANY

from .models import (
    Department,
    Dictionary,
    Database,
    Form,
    Group,
    Field,
    Report,
    Converter
)


class MainTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test1",
            password="Zz@12345",
        )
        self.user.save()
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def tearDown(self):
        self.client.force_authenticate(user=None)
        self.user.delete()

    def test_dictionary_list(self):
        dictionary = Dictionary.objects.create(
            title='Test dictionary',
            table_name='Test model'
        )

        dictionary.save()

        excepted_data = [
            {
                'id': ANY,
                'title': 'Test dictionary',
                'table_name': 'Test model',
            }
        ]

        response = self.client.get('/api/dictionaries/')

        assert response.status_code == 200

        self.assertListEqual(excepted_data, response.json())

    def test_database_list(self):
        db = Database.objects.create(
            pos=1,
            title='Test Database'
        )
        form = Form.objects.create(
            pos=1,
            title='Test Form',
            db=db,
            form_type=Form.FORM_TYPE[0][0]
        )
        group = Group.objects.create(
            pos=1,
            title='Test Group',
            form=form,
            is_multy=True,
            table_name='Group Model'
        )
        Field.objects.create(
            pos=1,
            title='Test Field',
            group=group,
            field_type=Field.FIELD_TYPE[0][0],
            field_name='Field Test Name',
            len=30,
            is_key=True,
            is_visible=True,
            is_enable=True,
            is_require=True,
            precision=10,
            is_duplicate=True
        )
        Report.objects.create(
            pos=1,
            title='Test Report',
            data={'data': 123},
            db=db
        )
        Converter.objects.create(
            pos=1,
            title='Test Converter',
            form=form,
            data={'data': 456},
            db=db
        )

        excepted_data = [
            {
                'id': ANY,
                'pos': 1,
                'title': 'Test Database',
                'forms': [
                    {
                        'id': ANY,
                        'pos': 1,
                        'title': 'Test Form',
                        'form_type': Form.FORM_TYPE[0][0],
                        'groups': [
                            {
                                'id': ANY,
                                'pos': 1,
                                'title': 'Test Group',
                                'is_multy': True,
                                'table_name': 'Group Model',
                                'fields': [
                                    {
                                        'id': ANY,
                                        'pos': 1,
                                        'group': group.id,
                                        'title': 'Test Field',
                                        'field_type': Field.FIELD_TYPE[0][0],
                                        'field_name': 'Field Test Name',
                                        'len': 30,
                                        'is_key': True,
                                        'is_visible': True,
                                        'is_enable': True,
                                        'is_require': True,
                                        'precision': 10,
                                        'is_duplicate': True
                                    }
                                ]
                            }
                        ]
                    }
                ],
                'reports': [
                    {
                        'id': ANY,
                        'pos': 1,
                        'title': 'Test Report',
                        'data': {'data': 123},
                        'template': ANY,
                        'db': db.id
                    }
                ],
                'converters': [
                    {
                        'id': ANY,
                        'pos': 1,
                        'title': 'Test Converter',
                        'form': ANY,
                        'data': {'data': 456},
                        'db': db.id
                    }
                ]
            }
        ]

        response = self.client.get('/api/databases/')

        assert response.status_code == 200

        self.assertListEqual(excepted_data, response.json())
