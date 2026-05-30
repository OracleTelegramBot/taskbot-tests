def test_task_service_reachable(driver, config):
    driver.get(f"{config['base_url']}/api/tasks/sprint/1")
    assert "ERR_" not in driver.page_source, "El servicio de tareas no es alcanzable"
