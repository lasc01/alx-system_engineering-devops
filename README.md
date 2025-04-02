# ALX System Engineering & DevOps

This repository contains my solutions and projects for the **ALX System Engineering & DevOps** track, covering shell scripting, networking, web infrastructure, debugging, and more.

---

## 📂 Repository Navigation

| Directory | Description |
|-----------|-------------|
| [0x00-shell_basics](0x00-shell_basics) | Shell scripting fundamentals (file manipulation, permissions, etc.). |
| [0x01-shell_permissions](0x01-shell_permissions) | Shell commands for file permissions (`chmod`, `chown`, etc.). |
| [0x02-shell_redirections](0x02-shell_redirections) | I/O redirections, pipes, and filters. |
| [0x03-shell_variables_expansions](0x03-shell_variables_expansions) | Environment variables and expansions in Bash. |
| [0x04-loops_conditions_and_parsing](0x04-loops_conditions_and_parsing) | Loops (`for`, `while`), conditionals (`if`), and text parsing. |
| [0x05-processes_and_signals](0x05-processes_and_signals) | Process management (`ps`, `kill`, signals). |
| [0x06-regular_expressions](0x06-regular_expressions) | Regex patterns for text processing (`grep`, `sed`). |
| [0x07-networking_basics](0x07-networking_basics) | Networking fundamentals (`ping`, `curl`, DNS). |
| [0x08-networking_basics_2](0x08-networking_basics_2) | Advanced networking (port listening, `netcat`). |
| [0x09-web_infrastructure_design](0x09-web_infrastructure_design) | Diagrams and explanations of web infrastructures. |
| [0x0A-configuration_management](0x0A-configuration_management) | Puppet manifests for automation. |
| [0x0B-ssh](0x0B-ssh) | SSH configuration and key management. |
| [0x0C-web_server](0x0C-web_server) | Nginx web server setup and domain configuration. |
| [0x0D-web_stack_debugging_0](0x0D-web_stack_debugging_0) | Debugging web server issues (e.g., 500 errors). |
| [0x0E-web_stack_debugging_1](0x0E-web_stack_debugging_1) | Advanced debugging for web stacks. |
| [0x0F-load_balancer](0x0F-load_balancer) | HAProxy load balancer configuration. |
| [0x10-https_ssl](0x10-https_ssl) | SSL/TLS setup and HTTPS redirection. |
| [0x12-web_stack_debugging_2](0x12-web_stack_debugging_2) | Concise fixes for web stack issues. |
| [0x13-firewall](0x13-firewall) | UFW firewall rules and port forwarding. |
| [0x14-mysql](0x14-mysql) | MySQL database setup and queries. |
| [0x15-api](0x15-api) | Python scripts to interact with REST APIs. |
| [0x16-api_advanced](0x16-api_advanced) | Advanced API usage (authentication, pagination). |
| [0x17-web_stack_debugging_3](0x17-web_stack_debugging_3) | Debugging Apache 500 errors. |
| [0x18-webstack_monitoring](0x18-webstack_monitoring) | Monitoring tools (Datadog, Prometheus). |
| [0x19-postmortem](0x19-postmortem) | Incident analysis reports (postmortems). |
| [0x1A-application_server](0x1A-application_server) | Gunicorn + Flask application server setup. |
| [0x1B-web_stack_debugging_4](0x1B-web_stack_debugging_4) | OS-level debugging (login issues, permissions). |
| [attack_is_the_best_defense](attack_is_the_best_defense) | Security-focused tasks (e.g., sniffing packets). |
| [command_line_for_the_win](command_line_for_the_win) | Command-line challenges (Bash/CMD). |
| [19-AZ](19-AZ) | Miscellaneous system engineering tasks. |

---

## 🛠️ Technologies & Tools
- **Shell Scripting**: Bash, Zsh  
- **Networking**: `curl`, `netcat`, DNS, HAProxy  
- **Web Servers**: Nginx, Apache  
- **Databases**: MySQL  
- **APIs**: Python (`requests`, `json`)  
- **DevOps**: Puppet, Docker, UFW  
- **Monitoring**: Datadog, Prometheus  

---

## 📌 Example Tasks
### 0x07-networking_basics
```bash
#!/bin/bash
# Pings an IP address passed as an argument 5 times.
ping -c 5 "$1"
