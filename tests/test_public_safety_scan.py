"""Regression checks for the public distribution boundary, using synthetic data."""
from pathlib import Path
import io
import sys
import tempfile
import unittest
import zipfile

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from public_safety_scan import REQUIRED_PACKAGE_ENTRIES, scan_package


class PackageSafetyTests(unittest.TestCase):
    def package_findings(self, extra_name, content=b"synthetic"):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "package.zip"
            with zipfile.ZipFile(path, "w") as package:
                for name in REQUIRED_PACKAGE_ENTRIES:
                    if name.endswith((".xlsx", ".docx")):
                        office = io.BytesIO()
                        with zipfile.ZipFile(office, "w") as document:
                            document.writestr("content.xml", "<synthetic />")
                        package.writestr(name, office.getvalue())
                    else:
                        package.writestr(name, "synthetic public template")
                package.writestr(extra_name, content)
            return scan_package(path)

    def test_public_template_is_accepted(self):
        self.assertEqual(self.package_findings("docs/public.md"), [])

    def test_corrupt_office_file_is_rejected(self):
        self.assertTrue(self.package_findings("docs/broken.docx", b"not an Office ZIP"))

    def test_build_only_content_is_rejected(self):
        self.assertTrue(self.package_findings("scripts/build.py"))

    def test_unsafe_member_paths_are_rejected(self):
        for name in ("../outside.md", "/absolute.md", "C:/outside.md", "docs/../scripts/tool.py", "docs\\private.md"):
            with self.subTest(name=name):
                self.assertTrue(self.package_findings(name), "Unsafe ZIP path accepted")


if __name__ == "__main__":
    unittest.main()
