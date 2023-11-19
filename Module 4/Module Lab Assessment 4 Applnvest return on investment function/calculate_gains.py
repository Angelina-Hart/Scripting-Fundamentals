multiplier_amount = 1000000

def calculate_gains(amount_inv=0.0):
    gain_margin = 0.001
    total_gains = 0
    total_amount = 0
    # initial investment must be at least $1000
    if amount_inv > 1000:
        if amount_inv >= multiplier_amount:
            gain_modifier = (amount_inv//multiplier_amount) * 0.01
            gain_margin += gain_modifier
            total_gains = amount_inv * gain_margin
            total_amount += amount_inv + total_gains
            return total_gains, total_amount, gain_margin
        else:
            total_gains = amount_inv * gain_margin
            total_amount += amount_inv + total_gains
            return total_gains, total_amount, gain_margin
print(calculate_gains(amount_inv=2000000))
