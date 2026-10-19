import unittest
from worker import matches, baseline_matches

class ProtectionTests(unittest.TestCase):
    def test_concurrent_alt_change_blocks(self):
        self.assertFalse(baseline_matches({'alt':'new staff alt','url':'a.jpg'}, {'alt':'old','url':'a.jpg'}))
    def test_concurrent_image_change_blocks(self):
        self.assertFalse(baseline_matches({'alt':'same','url':'new.jpg'}, {'alt':'same','url':'old.jpg'}))
    def test_both_fields_must_read_back(self):
        self.assertFalse(matches({'alt':'expected','url':'https://cdn.shopify.com/old.png'}, {'alt':'expected','filename':'new.png'}))
    def test_cdn_version_change_allowed_after_write(self):
        self.assertTrue(matches({'alt':'expected','url':'https://cdn.shopify.com/new.png?v=12'}, {'alt':'expected','filename':'new.png'}))

if __name__ == '__main__': unittest.main()

