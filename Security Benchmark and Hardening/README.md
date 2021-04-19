## Docker Bench and Hardening Guide 

**Step 1**

Run docker bench with the follwoing command.
```console
docker run --rm --net host --pid host --userns host --cap-add audit_control \

    -e DOCKER_CONTENT_TRUST=$DOCKER_CONTENT_TRUST \

    -v /etc:/etc:ro \

    -v /usr/bin/containerd:/usr/bin/containerd:ro \

    -v /usr/bin/runc:/usr/bin/runc:ro \

    -v /usr/lib/systemd:/usr/lib/systemd:ro \

    -v /var/lib:/var/lib:ro \

    -v /var/run/docker.sock:/var/run/docker.sock:ro \

    --label docker_bench_security \

    docker/docker-bench-security
 ```
**Step 2**
    
Refer to [Hardening Guide](https://github.com/TIC4302/video-streaming-bot/blob/master/Security%20Benchmark%20and%20Hardening/Hardening/Hardening%20Guide) for some tips on remediation
