import time

from plugins.feelback.run import clientMq

metadata = {
    "title": "feelback mqtt",
    "description": """
        This service listens to MQTT messages related to
        feelback operations and processes them accordingly.
        The service will listen to MQTT messages related
        to feelback operations and processes them accordingly.
        It will listen to MQTT messages related to feelback
        operations and processes them accordingly.
    """,
    "version": "1.0.0",
    "author": "Tanga Group",
    "type": "service",
    "module": "plugins",
    "moduleDir": "plugins/feelback",
    "status": True,
    "dependencies": ["mqtt"],
    "license": "MIT",
    "tags": ["mqtt", "service", "plugins"],
    "icon": "mdi:message-text",
    "homepage": "app/feelback",
    "documentation": "http://app.tangagroup.com/docs/feelback",
    "repository": "http://app.tangagroup.com/repo/feelback",
    "issues": "http://app.tangagroup.com/issues/feelback",
    "changelog": "http://app.tangagroup.com/changelog/feelback",
    "support": "http://app.tangagroup.com/support/feelback",
    "contact": {
        "email": "contact@tangagroup.com",
        "website": "http://app.tangagroup.com",
        "phone": "+1234567890",
    },
    "keywords": ["mqtt", "feelback", "service", "plugins"],
    "created_at": "2023-10-01T00:00:00Z",
    "updated_at": "2023-10-01T00:00:00Z",
    "license_url": "http://app.tangagroup.com/license",
}


def service_main(service):
    print("Service mqtt feelback demarrer")
    while service.running:
        try:
            clientMq.loopMqttServerListener()
        except Exception as e:
            print(f"Error in presence MQTT loop: {e}")
        time.sleep(1)  # Sleep to prevent tight loop in case of errors
    print("Service mqtt feelback arreter")
    clientMq.stop()
    print("MQTT client disconnected")
    return True
