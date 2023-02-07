#  Licensed under the Apache License, Version 2.0 (the "License"); you may
#  not use this file except in compliance with the License. You may obtain
#  a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#  WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#  License for the specific language governing permissions and limitations
#  under the License.
"""
Example script to show how to use Cloud L3 Firewall.
"""

import smc.examples

from smc.core.engine import Engine
from smc.core.engines import CloudSGSingleFW
from smc import session
from smc_info import *

if __name__ == '__main__':

    session.login(url=SMC_URL, api_key=API_KEY, verify=False, timeout=120, api_version=API_VERSION)
    print("session OK")


try:
    # Cloud engine creation
    print("Create cloud fw: Cloud Single firewall 1...")
    CloudSGSingleFW.create_dynamic(interface_id=0, name="Cloud Single firewall 1")

    # Should not use regular create method but create_dynamic instead
    # Since cloud firewall should use dynamic interface
    try:
        CloudSGSingleFW.create(name="test cloud name", mgmt_ip="1.1.1.1", mgmt_network="1.1.1.0/24")
    except Exception as e:
        print("regular create method not supported : %s" % str(e))
        print("The example can continue..")

    # Retrieve the Engine
    print("Get cloud fw...")
    engine = Engine("Cloud Single firewall 1")
    print(list(engine.nodes))

    print("======================================================================================")
    print("Firewall name: %s" % engine)
    print("Firewall REF: %s" % engine.href)
    for node in engine.nodes:
        print("Firewall nodes: %s" % node)
        print("Firewall nodes: %s" % node.href)
    print("======================================================================================")

    # Check node status
    print("Get node status...")
    for node in engine.nodes:
        print("Firewall node %s status: %s" % (node.name, str(node.status())))

except Exception as e:
    print("Example failed:" + str(e))
    exit(-1)

finally:
    engine = CloudSGSingleFW("Cloud Single firewall 1")
    engine.delete()
    session.logout()
