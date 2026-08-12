import unittest
from EmotionDetection.emotion_detector import emotion_detector

class TestEmotiionDetector (unittest.TestCase):
    def test_emotion_detector(self):
        result = emotion_detector("I love this new technology.")
        self.assertIsNotNone(result, "Is not None")

unittest.main()