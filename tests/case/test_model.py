import unittest

from app.helper.serialize import serialize_datetime
from tests.helpers import setUpApp, with_context, setUpDB, tearDownDB
from tests.case.helpers import CaseHelper


class TestCaseModel (unittest.TestCase):

    def setUp(self):
        setUpApp(self)
        setUpDB(self)

    def tearDown(self):
        tearDownDB(self)

    @with_context
    def test_to_json(self):
        case = CaseHelper._create_case()

        case_as_json = case.to_json()

        self.assertEqual(case_as_json["id"], CaseHelper._id)
        self.assertEqual(case_as_json["conveyancer_id"],
                         CaseHelper._conveyancer_id)
        self.assertEqual(case_as_json["status"], CaseHelper._status)
        self.assertEqual(case_as_json["last_updated"], serialize_datetime(
            CaseHelper._last_updated.isoformat()))
        self.assertEqual(case_as_json["created_on"], serialize_datetime(
            CaseHelper._created_on.isoformat()))

    @with_context
    def test_from_json(self):
        case = CaseHelper._create_case()

        self.assertEqual(case.id, CaseHelper._id)
        self.assertEqual(case.conveyancer_id, CaseHelper._conveyancer_id)
        self.assertEqual(case.status, CaseHelper._status)
        self.assertEqual(case.last_updated, CaseHelper._last_updated)
        self.assertEqual(case.created_on, CaseHelper._created_on)
