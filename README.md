<h1 align="center">System Maintenance Optimizer</h1>

<p align="center">
  <img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="AGPL-3.0 License">
  <img src="https://img.shields.io/badge/SMO-0.1.0-yellow.svg" alt="System Maintenance Optimizer Version">
</p>

<p align="center">A simple set of scripts to automate system maintenance tasks, such as cleaning up your system and monitoring its performance.</p>

<h2>Features</h2>
<ul>
  <li><b>Auto Cleanup</b>: Automatically removes unnecessary files to free up space.</li>
  <li><b>Performance Monitor</b>: Monitors and logs system performance in real time.</li>
</ul>

<h2>Supported Operating Systems</h2>
<ul>
  <li>Linux</li>
  <li>macOS</li>
  <li>Windows</li>
</ul>

<h2>Installation</h2>

<h3>Prerequisites</h3>
<p>Before you run the script, make sure the following software is installed:</p>
<ul>
  <li><b>Linux/macOS</b>: Ensure you have <code>bash</code> and required permissions.</li>
  <li><b>Windows</b>: Make sure you have Git Bash or another Bash-compatible shell (e.g., WSL or Cygwin).</li>
</ul>

<h3>Clone the repository</h3>
<p>To get started, clone the repository to your local machine:</p>

```bash
git clone https://github.com/anonymByte-404/system-maintenance-optimizer.git
cd system-maintenance-optimizer
```

<h2>Running the Scripts</h2>
<p>Once you have the repo set up, follow these steps to run the maintenance tasks:</p>

1. **Navigate to the project folder**:
    ```bash
    cd system-maintenance-optimizer
    ```

2. **Run the main script**:
  - For **Linux** or **macOS**, use:
    ```bash
    bash connect_all.sh
    ```

  - For **Windows**, use Git Bash and run:
    ```bash
    bash connect_all.sh
    ```

3. **Choose an option**: The script will prompt you with the following options:
    - **1.** Clean up system: Runs the cleanup task only.
    - **2.** Monitor system performance: Runs the performance monitoring task only.
    - **3.** Clean up system and monitor performance: Runs both tasks.
    - **4.** Exit: Exits the script.

4. **Follow the on-screen prompts**: Based on the OS detected, the script will automatically run the appropriate task for your platform.

<h2>Troubleshooting</h2>
<ul>
  <li><b>Windows users</b>: If you are encountering issues with Git Bash not recognizing Bash commands, ensure you are running the script from the Git Bash terminal, not the regular Command Prompt.</li>
  <li><b>Linux/macOS users</b>: Ensure <code>bash</code> is installed and that you have proper permissions to execute the scripts.</li>
</ul>

<h2>License</h2>
<p>This project is licensed under the MIT License - see the <a href="LICENSE">LICENSE</a> file for details.</p>

<h2>Contributing</h2>
<p>This project is for personal use and not accepting contributions currently. However, feel free to fork and customize it as needed.</p>
