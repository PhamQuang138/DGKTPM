import unittest

def calculate_rental_price(base_rate, days, is_weekend, is_holiday, delivery_distance, voucher_type, voucher_val):
    surcharge = 0
    if is_holiday:
        surcharge = base_rate * 0.30 * days
    elif is_weekend:
        surcharge = base_rate * 0.15 * days
    else:
        surcharge = 0

    total_rent = (base_rate * days) + surcharge

    if delivery_distance > 5:
        delivery_fee = (delivery_distance - 5) * 15000
    else:
        delivery_fee = 0

    insurance_fee = total_rent * 0.10

    if voucher_type == "PERCENT":
        discount = total_rent * (voucher_val / 100.0)
    elif voucher_type == "FIXED":
        discount = voucher_val
    else:
        discount = 0

    final_amount = total_rent + delivery_fee + insurance_fee - discount
    if final_amount < 0:
        final_amount = 0

    deposit_amount = final_amount * 0.30
    return final_amount, deposit_amount

class WhiteBoxBasisPathTests(unittest.TestCase):

    def test_path_1(self):
        """TC-WB-01: Path 1: Holiday, Distance > 5km, Voucher %, Positive Amount"""
        final, deposit = calculate_rental_price(1000000, 2, False, True, 10, "PERCENT", 10)
        self.assertEqual(final, 2675000)
        self.assertEqual(deposit, 802500)

    def test_path_2(self):
        """TC-WB-02: Path 2: Weekend, Distance <= 5km, Voucher FIXED, Positive Amount"""
        final, deposit = calculate_rental_price(1000000, 2, True, False, 4, "FIXED", 100000)
        self.assertEqual(final, 2430000)
        self.assertEqual(deposit, 729000)

    def test_path_3(self):
        """TC-WB-03: Path 3: Weekday, Distance <= 5km, No Voucher, Positive Amount"""
        final, deposit = calculate_rental_price(1000000, 1, False, False, 0, "NONE", 0)
        self.assertEqual(final, 1100000)
        self.assertEqual(deposit, 330000)

    def test_path_4(self):
        """TC-WB-04: Path 4: Weekday, Distance > 5km, Voucher %, Negative Amount -> 0"""
        final, deposit = calculate_rental_price(100000, 1, False, False, 6, "PERCENT", 200)
        self.assertEqual(final, 0)
        self.assertEqual(deposit, 0)

    def test_path_5(self):
        """TC-WB-05: Path 5: Weekend, Distance > 5km, Invalid Voucher"""
        final, deposit = calculate_rental_price(800000, 2, True, False, 8, "INVALID_CODE", 0)
        self.assertEqual(final, 2069000)
        self.assertEqual(deposit, 620700)

    def test_path_6(self):
        """TC-WB-06: Path 6: Holiday, Distance == 5km (Boundary), Voucher FIXED"""
        final, deposit = calculate_rental_price(1500000, 3, False, True, 5, "FIXED", 500000)
        self.assertEqual(final, 5935000)
        self.assertEqual(deposit, 1780500)

    def test_path_7(self):
        """TC-WB-07: Path 7: Weekday, Distance <= 5km, Voucher FIXED huge -> 0"""
        final, deposit = calculate_rental_price(500000, 1, False, False, 2, "FIXED", 1000000)
        self.assertEqual(final, 0)
        self.assertEqual(deposit, 0)

if __name__ == "__main__":
    unittest.main()

