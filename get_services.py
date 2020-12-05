import re
from pprint import pprint as pp


def loadconfig(filename):
    """This loads the config file and breaks it into lines

    :param filename: file location of the config file
    :return: a list containing the lines of the file with "\n" at the end
    :rtype: list
    """

    router_name = filename.split('.')[0]
    print(f'Current router: {router_name}')
    with open(filename, 'r') as file:
        contents = file.readlines()
    return contents


def vplssearch(text):
    """Uses a regex to find just vpls and its id

    :param text: config file location
    :return: a string of vpls and id eg. vpls 1929
    """
    vpls_pattern = re.compile(r'(vpls\s\d{2,9})')
    temp = vpls_pattern.search(text)

    if temp is not None:
        vpls_result = temp.group()
        return vpls_result
    else:
        pass


def vplsexit(text):
    """Uses a regex to find the end of the vpls context

    :param text: a string of text
    :return: a string of the word exit
    """
    vplsexit_pattern = re.compile(r'^\s{8}(exit)')
    temp = vplsexit_pattern.search(text)
    if temp is not None:
        vplsexit_result = temp.group()
        return vplsexit_result
    else:
        pass


def vprnexit(text):
    """Uses a regex to find the end of the vprn context

    :param text: a string of text
    :return: a string of the word exit
    """
    vprnexit_pattern = re.compile(r'^\s{8}(exit)')
    temp = vprnexit_pattern.search(text)
    if temp is not None:
        vprnexit_result = temp.group()
        return vprnexit_result
    else:
        pass


def vprnsearch(text):
    """Uses a regex to find just vprn and its id

    :param text: config file location
    :return: a string of vprn and id eg. vprn 1929
    """
    vprn_pattern = re.compile(r'(vprn\s\d{2,9})')
    temp = vprn_pattern.search(text)

    if temp is not None:
        vprn_result = temp.group()
        return vprn_result
    else:
        pass


def find_servicedesc(text):
    servicedesc_pattern = re.compile(r'^\s{12}description\s\"(.+)\"')
    temp = servicedesc_pattern.search(text)
    if temp is not None:
        servicedesc = temp.group(1)
        return servicedesc
    else:
        pass


def sapinfo(text):
    sap_info = {}
    sap_pattern = re.compile(r'(sap\s(\d/[0-9X]?\d/[0-9]?\d|\w+-\d)[:]?([\d+]+)?)')
    temp = sap_pattern.search(text)
    if temp is not None:
        sap = str(temp.group())
        sap_info[sap] = {}
        sap_info[sap]['vlan'] = temp.group(3)
        sap_info[sap]['port'] = temp.group(2)
        sap_info[sap]['qos'] = None
        return sap_info, sap
    else:
        pass


def findqos(text):
    qos_pattern = re.compile(r'qos\s(\d+)')
    temp = qos_pattern.search(text)
    if temp is not None:
        qos = temp.group(1)
        return qos
    else:
        pass


def findspokesdp(text):
    spokesdp_pattern = re.compile(r'spoke-sdp\s(\d+:\d+)')
    temp = spokesdp_pattern.search(text)
    if temp is not None:
        spokesdp = temp.group(1)
        return spokesdp
    else:
        pass


def finddescription(text):
    desc_pattern = re.compile(r'description\s\"(.+)\"')
    temp = desc_pattern.search(text)
    if temp is not None:
        desc = temp.group(1)
        return desc
    else:
        pass


def find_servicename(text):
    servicename_pattern = re.compile(r'service-name\s\"(.+)\"')
    temp = servicename_pattern.search(text)
    if temp is not None:
        servicename = temp.group(1)
        return servicename
    else:
        pass


def find_servicemtu(text):
    servicemtu_pattern = re.compile(r'service-mtu\s\"(.+)\"')
    temp = servicemtu_pattern.search(text)
    if temp is not None:
        servicemtu = temp.group(1)
        return servicemtu
    else:
        pass


def allow_ip_int(text):
    allow_ip_int_pattern = re.compile(r'allow-ip-int-binding')
    temp = allow_ip_int_pattern.search(text)
    if temp is not None:
        allow_ip_int = temp.group()
        return allow_ip_int
    else:
        pass


def find_service_shutdown(text):
    service_shutdown_pattern = re.compile(r'^\s{12}(shutdown)')
    temp = service_shutdown_pattern.search(text)
    if temp is not None:
        service_shutdown = temp.group(1)
        return service_shutdown
    else:
        pass


def findmeshsdp(text):
    meshsdp_pattern = re.compile(r'mesh-sdp\s(\d+:\d+)')
    temp = meshsdp_pattern.search(text)
    if temp is not None:
        meshsdp = temp.group(1)
        return meshsdp
    else:
        pass


def find_service(text):
    """Uses a regex to find just service and its id

    :param text: config file location
    :return: a string of service and id eg. vpls 1929
    """
    service_pattern = re.compile(r'(\b(vpls|epipe|vprn)\s\d{1,9})')
    temp = service_pattern.search(text)

    if temp is not None:
        service_result = temp.group()
        return service_result
    else:
        pass


def find_service_exit(text):
    """Uses a regex to find the end of the service context

    :param text: a string of text
    :return: a string of the word exit
    """
    service_exit_pattern = re.compile(r'^\s{8}(exit)')
    temp = service_exit_pattern.search(text)
    if temp is not None:
        service_exit_result = temp.group()
        return service_exit_result
    else:
        pass


def find_shutdown(text):
    """Uses a regex to find the word shutdown on a line

    :param text: a string of text
    :return: a string of the word exit
    """
    shutdown_pattern = re.compile(r'shutdown')
    temp = shutdown_pattern.search(text)
    if temp is not None:
        shutdown_result = temp.group()
        return shutdown_result
    else:
        pass


def find_as_number(text):
    as_number_pattern = re.compile(r'autonomous-system\s(\d+)')
    temp = as_number_pattern.search(text)
    if temp is not None:
        as_number = temp.group(1)
        return as_number
    else:
        pass


def find_rd(text):
    rd_pattern = re.compile(r'route-distinguisher\s((\d+|\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):\d+)')
    temp = rd_pattern.search(text)
    if temp is not None:
        rd = temp.group(1)
        return rd
    else:
        pass


def find_if(text):
    if_pattern = re.compile(r'^\s{12}interface\s\"(.+)\"')
    temp = if_pattern.search(text)
    if temp is not None:
        if_result = temp.group(1)
        return if_result
    else:
        pass


def if_vpls(text):
    if_vpls_pattern = re.compile(r'^\s{16}vpls\s\"(.+)\"')
    temp = if_vpls_pattern.search(text)
    if temp is not None:
        if_vpls = temp.group(1)
        return if_vpls
    else:
        pass


def if_address(text):
    ifaddress_pattern = re.compile(r'^\s{16}address\s(\d+\.\d+\.\d+\.\d+/\d+)')
    temp = ifaddress_pattern.search(text)
    if temp is not None:
        if_address = temp.group(1)
        return if_address
    else:
        pass


file = 'test_router.txt'

file_contents = loadconfig(file)
services = {}
service_list = []
n = 0
# print(file_contents)
for line in file_contents:
    n += 1
    if find_service(line) is not None:
        service = find_service(line)

        if 'vpls' in service:
            service_list.append(tuple([service, n]))
            services.setdefault(service, {'sap': {}})

            nn = n
            for lines_under_context in file_contents[nn:]:
                nn += 1

                service_exit = find_service_exit(lines_under_context)
                if service_exit is not None:
                    break

                service_shutdown = find_service_shutdown(lines_under_context)
                if service_shutdown is not None:
                    services[service]['shutdown'] = True
                    continue

                service_name = find_servicename(lines_under_context)
                if service_name is not None:
                    services[service]['service-name'] = service_name
                    # print(f'service name {service_name} of {service} is on line {nn}')
                    continue

                service_desc = find_servicedesc(lines_under_context)
                if service_desc is not None:
                    services[service]['description'] = service_desc
                    continue

                allow_ip_int_binding = allow_ip_int(lines_under_context)
                if allow_ip_int_binding is not None:
                    services[service]['allow-ip-int-binding'] = True
                    continue

                service_mtu = find_servicemtu(lines_under_context)
                if service_mtu is not None:
                    services[service]['service-mtu'] = service_mtu
                    continue

                if sapinfo(lines_under_context) is not None:
                    sap = sapinfo(lines_under_context)
                    services[service]['sap'].update(sap[0])
                    continue

                sapdesc = finddescription(lines_under_context)
                if sapdesc is not None:
                    services[service]['sap'][sap[1]]['description'] = sapdesc
                    continue

                qos = findqos(lines_under_context)
                if qos is not None:
                    services[service]['sap'][sap[1]]['qos'] = qos
                    continue

                if find_shutdown(lines_under_context) is not None:
                    if 'sap' in file_contents[nn-2]:
                        services[service]['sap'][sap[1]]['shutdown'] = True
                        # print(f'{sap[1]} on line {nn-2} is shutdown')
                    continue

                spokesdp = findspokesdp(lines_under_context)
                if spokesdp is not None:
                    if 'spoke-sdp' in services[service]:
                        services[service]['spoke-sdp'].append(spokesdp)
                        continue
                    else:
                        services[service]['spoke-sdp'] = []
                        services[service]['spoke-sdp'].append(spokesdp)
                        continue

                meshsdp = findmeshsdp(lines_under_context)
                if meshsdp is not None:
                    if 'mesh-sdp' in services[service]:
                        services[service]['mesh-sdp'].append(meshsdp)
                        continue
                    else:
                        services[service]['mesh-sdp'] = []
                        services[service]['mesh-sdp'].append(meshsdp)
                        continue

        if 'vprn' in service:
            service_list.append(tuple([service, n]))
            services.setdefault(service, {'interfaces': {}})

            nn = n
            for lines_under_context in file_contents[nn:]:
                nn += 1

                service_exit = find_service_exit(lines_under_context)
                if service_exit is not None:
                    break

                service_shutdown = find_service_shutdown(lines_under_context)
                if service_shutdown is not None:
                    services[service]['shutdown'] = True
                    continue

                service_name = find_servicename(lines_under_context)
                if service_name is not None:
                    services[service]['service-name'] = service_name
                    continue

                service_desc = find_servicedesc(lines_under_context)
                if service_desc is not None:
                    services[service]['description'] = service_desc
                    continue

                rd = find_rd(lines_under_context)
                if rd is not None:
                    services[service]['rd'] = rd
                    continue

                as_number = find_as_number(lines_under_context)
                if as_number is not None:
                    services[service]['autonomous-system'] = as_number
                    continue

                if find_if(lines_under_context) is not None:
                    iface = find_if(lines_under_context)
                    services[service]['interfaces'][iface] = {'address': ''}
                    continue

                ifaddress = if_address(lines_under_context)
                if ifaddress is not None:
                    services[service]['interfaces'][iface]['address'] = ifaddress
                    continue

                if if_vpls(lines_under_context) is not None:
                    ifvpls = if_vpls(lines_under_context)
                    services[service]['interfaces'][iface]['vpls'] = ifvpls
                    continue

                if sapinfo(lines_under_context) is not None:
                    sap = sapinfo(lines_under_context)
                    services[service]['interfaces'][iface]['sap'] = {}
                    services[service]['interfaces'][iface]['sap'].update(sap[0])
                    continue

                if find_shutdown(lines_under_context) is not None:
                    if 'interfaces' in file_contents[nn-2]:
                        services[service]['interfaces'][iface]['shutdown'] = True
                        continue

                    if 'sap' in file_contents[nn-2]:
                        services[service]['interfaces'][iface]['sap'][sap[1]]['shutdown'] = True
                        continue
                    continue

                if finddescription(lines_under_context) is not None:
                    if 'sap' in file_contents[nn-2]:
                        sapdesc = finddescription(lines_under_context)
                        services[service]['interfaces'][iface]['sap'][sap[1]]['description'] = sapdesc
                        continue

                qos = findqos(lines_under_context)
                if qos is not None:
                    services[service]['interfaces'][iface]['sap'][sap[1]]['qos'] = qos
                    continue

                spokesdp = findspokesdp(lines_under_context)
                if spokesdp is not None:
                    services[service]['interfaces'][iface]['spoke-sdp'] = spokesdp
                    continue

        if 'epipe' in service:
            service_list.append(tuple([service, n]))
            services.setdefault(service, {'sap': {}})

            nn = n
            for lines_under_context in file_contents[nn:]:
                nn += 1

                service_exit = find_service_exit(lines_under_context)
                if service_exit is not None:
                    break

                service_shutdown = find_service_shutdown(lines_under_context)
                if service_shutdown is not None:
                    services[service]['shutdown'] = True
                    continue

                service_name = find_servicename(lines_under_context)
                if service_name is not None:
                    services[service]['service-name'] = service_name
                    # print(f'service name {service_name} of {service} is on line {nn}')
                    continue

                service_desc = find_servicedesc(lines_under_context)
                if service_desc is not None:
                    services[service]['description'] = service_desc
                    continue

                service_mtu = find_servicemtu(lines_under_context)
                if service_mtu is not None:
                    services[service]['service-mtu'] = service_mtu
                    continue

                if sapinfo(lines_under_context) is not None:
                    sap = sapinfo(lines_under_context)
                    services[service]['sap'].update(sap[0])
                    continue

                sapdesc = finddescription(lines_under_context)
                if sapdesc is not None:
                    services[service]['sap'][sap[1]]['description'] = sapdesc
                    continue

                qos = findqos(lines_under_context)
                if qos is not None:
                    services[service]['sap'][sap[1]]['qos'] = qos
                    continue

                if find_shutdown(lines_under_context) is not None:
                    if 'sap' in file_contents[nn-2]:
                        services[service]['sap'][sap[1]]['shutdown'] = True
                    continue

                spokesdp = findspokesdp(lines_under_context)
                if spokesdp is not None:
                    if 'spoke-sdp' in services[service]:
                        services[service]['spoke-sdp'].append(spokesdp)
                        continue
                    else:
                        services[service]['spoke-sdp'] = []
                        services[service]['spoke-sdp'].append(spokesdp)
                        continue

                meshsdp = findmeshsdp(lines_under_context)
                if meshsdp is not None:
                    if 'mesh-sdp' in services[service]:
                        services[service]['mesh-sdp'].append(meshsdp)
                        continue
                    else:
                        services[service]['mesh-sdp'] = []
                        services[service]['mesh-sdp'].append(meshsdp)
                        continue

pp(services)
