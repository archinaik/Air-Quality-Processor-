import unittest
import pandas as pd

class TestDataFrame(unittest.TestCase):
    def test_combined_dataframe(self):
        df_temp = pd.DataFrame({
            "Value": [20.0, 25.5],
            "Time": ["10:00", "11:00"]
        })
        df_temp.insert(0, "pollutant", "TEMPERATURE")

        df_so2 = pd.DataFrame({
            "Value": [10.0, 15.0],
            "Time": ["10:00", "11:00"]
        })
        df_so2.insert(0, "pollutant", "SO2")

        combined_df = pd.concat([df_temp, df_so2], ignore_index=True)

        self.assertEqual(len(combined_df), 4)
        self.assertIn("pollutant", combined_df.columns)

        temp_values = combined_df[combined_df["pollutant"] == "TEMPERATURE"]["Value"]
        self.assertEqual(temp_values.max(), 25.5)
        self.assertEqual(temp_values.min(), 20.0)

        so2_values = combined_df[combined_df["pollutant"] == "SO2"]["Value"]
        self.assertEqual(so2_values.max(), 15.0)
        self.assertEqual(so2_values.min(), 10.0)

if __name__ == "__main__":
    unittest.main()
