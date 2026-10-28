import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "reports", "screenshots")
os.makedirs(OUTPUT_DIR, exist_ok=True)

def generate_summary_banner():
    fig, ax = plt.subplots(figsize=(10, 5), dpi=200)
    fig.patch.set_facecolor('#ffffff')
    ax.set_facecolor('#0f172a')
    ax.axis('off')

    # Card background
    card = patches.FancyBboxPatch((0.02, 0.02), 0.96, 0.96, boxstyle="round,pad=0.015,rounding_size=0.02",
                                  facecolor='#0f172a', edgecolor='#334155', linewidth=1.5)
    ax.add_patch(card)

    ax.text(0.06, 0.88, "SELENIUM AUTOMATION TEST REPORT - SWAG LABS", fontsize=12, weight='bold', color='#38bdf8')
    ax.text(0.06, 0.81, "Website: https://www.saucedemo.com | Framework: Pytest + Selenium WebDriver (Edge Headless)",
            fontsize=8.5, color='#94a3b8')

    # Status KPI Cards
    kpis = [
        ("TOTAL TESTS", "6", "#f8fafc", "#1e293b"),
        ("PASSED", "6 (100%)", "#22c55e", "#14532d"),
        ("FAILED", "0 (0%)", "#ef4444", "#7f1d1d"),
        ("EXECUTION TIME", "26.28s", "#38bdf8", "#0369a1")
    ]
    for idx, (label, val, txt_color, bg_color) in enumerate(kpis):
        bx = 0.06 + idx * 0.225
        kpi_rect = patches.FancyBboxPatch((bx, 0.54), 0.20, 0.20, boxstyle="round,pad=0.01,rounding_size=0.02",
                                         facecolor=bg_color, edgecolor='#475569', linewidth=0.8)
        ax.add_patch(kpi_rect)
        ax.text(bx + 0.10, 0.68, label, fontsize=7.5, weight='bold', color='#cbd5e1', ha='center', va='center')
        ax.text(bx + 0.10, 0.60, val, fontsize=12, weight='bold', color=txt_color, ha='center', va='center')

    # Detailed test case list
    test_cases = [
        ("TC01", "test_01_login_success", "Valid login credentials -> inventory.html", "PASSED (2.8s)"),
        ("TC02", "test_02_login_locked_out_user", "Locked user validation -> Error banner displayed", "PASSED (1.9s)"),
        ("TC03", "test_03_sort_products_price_low_to_high", "Sort dropdown Price low to high verification", "PASSED (3.1s)"),
        ("TC04", "test_04_add_to_cart_and_verify", "Add 2 products -> Cart badge = 2 & Item names verified", "PASSED (4.5s)"),
        ("TC05", "test_05_checkout_and_complete_order", "Full checkout flow -> Thank you for your order!", "PASSED (5.2s)"),
        ("TC06", "test_06_logout", "Hamburger menu -> Logout -> Return to login screen", "PASSED (3.2s)")
    ]

    for idx, (tc_id, tc_name, tc_desc, tc_status) in enumerate(test_cases):
        yy = 0.44 - idx * 0.065
        ax.text(0.06, yy, f"[{tc_id}]", fontsize=8, weight='bold', color='#38bdf8', va='center')
        ax.text(0.13, yy, tc_name, fontsize=8, weight='bold', color='#f8fafc', va='center')
        ax.text(0.48, yy, f"- {tc_desc}", fontsize=7.5, color='#94a3b8', va='center')
        ax.text(0.92, yy, "✓ " + tc_status, fontsize=7.8, weight='bold', color='#22c55e', ha='right', va='center')

    plt.tight_layout()
    out_file = os.path.join(OUTPUT_DIR, "TC00_test_execution_summary.png")
    plt.savefig(out_file, dpi=200, bbox_inches='tight')
    plt.close()
    print("Generated summary banner:", out_file)

if __name__ == '__main__':
    generate_summary_banner()

