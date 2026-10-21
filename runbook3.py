from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.tasks.files import write_file
from nornir_utils.plugins.functions import print_result
from nornir.core.exceptions import NornirExecutionError

nr = InitNornir(config_file="config.yaml")

cmd_list = ["show ip int brief", "show version", "show clock"]
def show_command_test(task):
    for cmd in cmd_list:
        response = task.run(task=send_command, command= cmd)
        task.run(task=write_file, content= response.result, filename = "interface.txt")

results = nr.run(task=show_command_test)

print_result(results)

failure = nr.data.failed_hosts

if failure:
    raise NornirExecutionError("Nornir detected failure")
