# Steps to set up your own PS2 DNS with DNAS replacement server
1. Stop systemd resolvd
```
sudo systemctl stop systemd-resolved.service
```

2. Edit `config.json` to set your hostnames and IPs

3. Run `build.sh`

4. Run `run.sh`

