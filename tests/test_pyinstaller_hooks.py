"""Regression tests for the frozen app's custom PyInstaller hooks."""

from pathlib import Path
import runpy
import unittest


ROOT_DIR = Path(__file__).resolve().parents[1]


class TestTransformersHook(unittest.TestCase):
    def test_keeps_runtime_scanned_model_sources_on_disk(self):
        hook = runpy.run_path(
            str(ROOT_DIR / "pyinstaller_hooks" / "hook-transformers.py")
        )

        self.assertEqual(
            hook["module_collection_mode"],
            {
                "transformers.models.auto": "pyz+py",
                "transformers.models.encoder_decoder": "pyz+py",
                "transformers.models.qwen2": "pyz+py",
                "transformers.models.whisper": "pyz+py",
            },
        )
        self.assertTrue(
            any(
                Path(source).name == "__init__.py"
                and destination == "transformers/models"
                for source, destination in hook["datas"]
            )
        )


if __name__ == "__main__":
    unittest.main()
