# -------------------------------------------------------------------------------------------------
#  Copyright (C) 2015-2020 Nautech Systems Pty Ltd. All rights reserved.
#  https://nautechsystems.io
#
#  Licensed under the GNU Lesser General Public License Version 3.0 (the "License");
#  You may not use this file except in compliance with the License.
#  You may obtain a copy of the License at https://www.gnu.org/licenses/lgpl-3.0.en.html
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
# -------------------------------------------------------------------------------------------------

import unittest

from nautilus_trader.indicators.donchian_channel import DonchianChannel


class DonchianChannelTests(unittest.TestCase):

    # Fixture Setup
    def setUp(self):
        # Arrange
        self.dc = DonchianChannel(10)

    def test_name_returns_expected_name(self):
        # Act
        # Assert
        self.assertEqual("DonchianChannel", self.dc.name)

    def test_str_repr_returns_expected_string(self):
        # Act
        # Assert
        self.assertEqual("DonchianChannel(10)", str(self.dc))
        self.assertEqual("DonchianChannel(10)", repr(self.dc))

    # def test_repr_returns_expected_string(self):
    #     # Act
    #     # Assert
    #     self.assertTrue(repr(self.kc).startswith(
    #         "<KeltnerChannel(10, 2.5, EXPONENTIAL, SIMPLE, True, 0.0) object at"))
    #     self.assertTrue(repr(self.kc).endswith('>'))
    #
    # def test_period_returns_expected_value(self):
    #     # Act
    #     # Assert
    #     self.assertEqual(10, self.kc.period)
    #
    # def test_k_multiple_returns_expected_value(self):
    #     # Act
    #     # Assert
    #     self.assertEqual(2.5, self.kc.k_multiplier)
    #
    # def test_initialized_without_inputs_returns_false(self):
    #     # Act
    #     # Assert
    #     self.assertEqual(False, self.kc.initialized)
    #
    # def test_initialized_with_required_inputs_returns_true(self):
    #     # Arrange
    #     self.kc.update_raw(1.00020, 1.00000, 1.00010)
    #     self.kc.update_raw(1.00020, 1.00000, 1.00010)
    #     self.kc.update_raw(1.00020, 1.00000, 1.00010)
    #     self.kc.update_raw(1.00020, 1.00000, 1.00010)
    #     self.kc.update_raw(1.00020, 1.00000, 1.00010)
    #     self.kc.update_raw(1.00020, 1.00000, 1.00010)
    #     self.kc.update_raw(1.00020, 1.00000, 1.00010)
    #     self.kc.update_raw(1.00020, 1.00000, 1.00010)
    #     self.kc.update_raw(1.00020, 1.00000, 1.00010)
    #     self.kc.update_raw(1.00020, 1.00000, 1.00010)
    #
    #     # Act
    #     # Assert
    #     self.assertEqual(True, self.kc.initialized)
    #
    # def test_value_with_one_input_returns_expected_value(self):
    #     # Arrange
    #     self.kc.update_raw(1.00020, 1.00000, 1.00010)
    #
    #     # Act
    #     # Assert
    #     self.assertEqual(1.0006, self.kc.value_upper_band)
    #     self.assertEqual(1.0001, self.kc.value_middle_band)
    #     self.assertEqual(0.9996, self.kc.value_lower_band)
    #
    # def test_value_with_three_inputs_returns_expected_value(self):
    #     # Arrange
    #     self.kc.update_raw(1.00020, 1.00000, 1.00010)
    #     self.kc.update_raw(1.00030, 1.00010, 1.00020)
    #     self.kc.update_raw(1.00040, 1.00020, 1.00030)
    #
    #     # Act
    #     # Assert
    #     self.assertEqual(1.0006512396694212, self.kc.value_upper_band)
    #     self.assertEqual(1.0001512396694212, self.kc.value_middle_band)
    #     self.assertEqual(0.9996512396694213, self.kc.value_lower_band)
    #
    # def test_reset_successfully_returns_indicator_to_fresh_state(self):
    #     # Arrange
    #     self.kc.update_raw(1.00020, 1.00000, 1.00010)
    #     self.kc.update_raw(1.00030, 1.00010, 1.00020)
    #     self.kc.update_raw(1.00040, 1.00020, 1.00030)
    #
    #     # Act
    #     self.kc.reset()  # No assertion errors.