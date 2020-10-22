#!/usr/bin/env python

import time
import jenkins

from pprint import pprint

def main() :
    username = 'xxxxxx'
    api_token = 'yyyyyy'
    
    server = \
        jenkins.Jenkins('http://localhost:8080',
            username=username,
            password=api_token
        )

    user = server.get_whoami()
    version = server.get_version()
    print('Hello {0} from Jenkins {1}'.format(user['fullName'], version))

    jobs = server.get_jobs()
    for job in jobs :
        print(job)

    job = 'cellos_cmake_kernel'

    print("build {0}".format(job))
   
    job_info = server.get_job_info(job)

    old_build_number = job_info['lastCompletedBuild']['number']
    
    print("old_build_number : {0}".format(old_build_number))

    build_info = server.get_build_info(job, old_build_number)
    print(build_info)
    
    server.build_job(job,
        {
            'TARGET' : 'kernel'
        }
    )

    while 1:
        job_info = server.get_job_info(job)
        last_build_number = job_info['lastCompletedBuild']['number']
        if old_build_number != last_build_number :
            build_info = server.get_build_info(job, last_build_number)
            print("finished")
            pprint(build_info)
            break
        else :
            print("last_build_number : {0}".format(last_build_number))
            print("not finished, wait 3 sec")
            time.sleep(3)

    log = server.get_build_console_output(job, last_build_number)
    print(log)
    print('result : {0}'.format(build_info['result']))

if __name__ == '__main__' :
    main()

