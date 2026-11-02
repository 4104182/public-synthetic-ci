"""PUBLIC simulated-input unit tests. No private app source, real keys or data."""
import hashlib
import re
import unittest
from pathlib import PurePosixPath


def synthetic_source_label(name: str) -> str:
    """Validate only public generated fixture labels; never map real server paths."""
    if not re.fullmatch(r"fixture-[a-z][a-z0-9-]{0,30}", name):
        raise ValueError("invalid public fixture label")
    return name


def synthetic_checksum(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def public_artifact_name(name: str) -> str:
    """Only synthetic reports; never copy APKs, logs or source from private repos."""
    p = PurePosixPath(name)
    if (p.is_absolute() or len(p.parts) != 1 or p.name not in
            {"synthetic-unit-report.json", "synthetic-contract-results.txt"}):
        raise ValueError("artifact is not an approved public synthetic report")
    return p.name


class SyntheticPublicBoundaryTests(unittest.TestCase):
    def test_fixture_label(self):
        self.assertEqual(synthetic_source_label("fixture-example"), "fixture-example")

    def test_reject_non_fixture_label(self):
        for name in ("real-wallet", "fixture-../secret", "", "fixture-KEY_0"):
            with self.subTest(name=name), self.assertRaises(ValueError):
                synthetic_source_label(name)

    def test_deterministic_fake_hash(self):
        self.assertEqual(synthetic_checksum(b"sample-only"), hashlib.sha256(b"sample-only").hexdigest())

    def test_only_public_synthetic_report(self):
        self.assertEqual(public_artifact_name("synthetic-unit-report.json"), "synthetic-unit-report.json")

    def test_deny_private_apk_and_nested_paths(self):
        for name in ("wallet-debug.apk", "internal/report.txt", "../private", "/tmp/result"):
            with self.subTest(name=name), self.assertRaises(ValueError):
                public_artifact_name(name)


if __name__ == "__main__":
    unittest.main()
