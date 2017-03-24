import unittest
import mock

from filerm import rm

class Test(unittest.TestCase):

    @mock.patch('filerm.os')
    def test_rm(self, mock_os):
        rm("test_file")
        mock_os.remove.assert_called_with("test_file")


if __name__ == "__main__":
    unittest.main()
