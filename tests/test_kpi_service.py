def test_kpi_health(driver, config):
    driver.get(f"{config['base_url']}/api/kpis/sprints/activoss")
    assert "ERR_" not in driver.page_source, "El servicio de KPIs no es alcanzable"
