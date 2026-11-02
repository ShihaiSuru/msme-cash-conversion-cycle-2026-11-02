#!/usr/bin/env python3
"""
MSME Cash Conversion Cycle (CCC) and Working Capital Gap Analyzer
Starter script for Indian MSMEs — practical, commented, and ready to extend.

CCC = Days Inventory Outstanding (DIO) + Days Sales Outstanding (DSO) - Days Payable Outstanding (DPO)

Working Capital Gap ≈ Average Daily Sales × CCC
"""

from dataclasses import dataclass
from typing import List


@dataclass
class MSMEFinancials:
    name: str
    annual_sales: float          # ₹
    average_inventory: float      # ₹
    average_receivables: float    # ₹
    average_payables: float       # ₹
    cogs: float                   # Cost of Goods Sold (₹) — used for DIO


def calculate_dio(average_inventory: float, cogs: float) -> float:
    """Days Inventory Outstanding."""
    if cogs <= 0:
        return 0.0
    return (average_inventory / cogs) * 365


def calculate_dso(average_receivables: float, annual_sales: float) -> float:
    """Days Sales Outstanding."""
    if annual_sales <= 0:
        return 0.0
    return (average_receivables / annual_sales) * 365


def calculate_dpo(average_payables: float, cogs: float) -> float:
    """Days Payable Outstanding."""
    if cogs <= 0:
        return 0.0
    return (average_payables / cogs) * 365


def calculate_ccc(dio: float, dso: float, dpo: float) -> float:
    """Cash Conversion Cycle in days."""
    return dio + dso - dpo


def estimate_working_capital_gap(annual_sales: float, ccc_days: float) -> float:
    """Rough working capital gap in ₹."""
    average_daily_sales = annual_sales / 365
    return average_daily_sales * ccc_days


def risk_flags(dio: float, dso: float, dpo: float, ccc: float) -> List[str]:
    """Simple, practical risk indicators for Indian MSMEs."""
    flags = []
    if dso > 60:
        flags.append("High DSO (>60 days) — collections are slow; consider stricter credit terms or better follow-up.")
    if dio > 45:
        flags.append("Elevated DIO (>45 days) — inventory may be tying up excess cash.")
    if dpo < 30:
        flags.append("Short DPO (<30 days) — paying suppliers faster than necessary; negotiate better terms.")
    if ccc > 75:
        flags.append("Stretched CCC (>75 days) — significant working capital pressure. Priority: accelerate collections and optimize inventory.")
    if not flags:
        flags.append("CCC looks reasonably managed for an MSME. Continue monitoring monthly.")
    return flags


def analyze(msme: MSMEFinancials) -> None:
    """Run full analysis and print a clear report."""
    dio = calculate_dio(msme.average_inventory, msme.cogs)
    dso = calculate_dso(msme.average_receivables, msme.annual_sales)
    dpo = calculate_dpo(msme.average_payables, msme.cogs)
    ccc = calculate_ccc(dio, dso, dpo)
    gap = estimate_working_capital_gap(msme.annual_sales, ccc)
    flags = risk_flags(dio, dso, dpo, ccc)

    print("=" * 60)
    print(f"Cash Conversion Cycle Analysis: {msme.name}")
    print("=" * 60)
    print(f"Annual Sales:          ₹{msme.annual_sales:,.0f}")
    print(f"COGS:                  ₹{msme.cogs:,.0f}")
    print(f"Avg Inventory:         ₹{msme.average_inventory:,.0f}")
    print(f"Avg Receivables:       ₹{msme.average_receivables:,.0f}")
    print(f"Avg Payables:          ₹{msme.average_payables:,.0f}")
    print("-" * 60)
    print(f"Days Inventory Outstanding (DIO): {dio:.1f} days")
    print(f"Days Sales Outstanding (DSO):     {dso:.1f} days")
    print(f"Days Payable Outstanding (DPO):   {dpo:.1f} days")
    print(f"Cash Conversion Cycle (CCC):      {ccc:.1f} days")
    print(f"Estimated Working Capital Gap:    ₹{gap:,.0f}")
    print("-" * 60)
    print("Risk / Action Flags:")
    for flag in flags:
        print(f"  • {flag}")
    print("=" * 60)
    print("Note: Educational starter only. Replace sample data with real GST / bank / invoice figures.")
    print("Not financial advice.")


if __name__ == "__main__":
    # Realistic sample for a small Indian MSME (trading / light manufacturing)
    sample = MSMEFinancials(
        name="Sample MSME – Auto Components Supplier",
        annual_sales=2_40_00_000,      # ₹2.4 crore
        cogs=1_68_00_000,              # ~70% of sales
        average_inventory=28_00_000,   # ~60 days of COGS roughly
        average_receivables=42_00_000, # ~64 days of sales
        average_payables=18_00_000,    # ~39 days of COGS
    )

    analyze(sample)

    print("\n--- Try your own numbers ---")
    print("Edit the MSMEFinancials object above or call analyze() with your data.")
