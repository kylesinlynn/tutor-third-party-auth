# Third Party Auth Plugin
Customizable Tutor Plugin for Open edX

# Content
- [Third Party Auth Plugin](#third-party-auth-plugin)
- [Content](#content)
- [Setup](#setup)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

# Setup
> This is the `main` branch which is intended to be used for development purpose. Some bugs and unexpected behaviors will occur while installing from this branch.

1. Clone the git repository into `tutor plugins root` using the following command.
   ```bash
   git clone https://github.com/kylesinlynn/openedx/tutor-third-party-auth.git && mv "$(pwd)/tutor-third-party-auth/third-party-auth.py" "$(tutor plugins printroot)"
   ```

2. List the installed plugins.
   ```bash
   tutor plugins list
   ```

3. Enable the plugins if you found `third-party-auth` plugin.
   ```bash
   tutor plugins enable third-party-auth
   ```

# Troubleshooting
Create an issue upon your error that is associated with this project.

# Contributing
Feel free to fork and create pull requests. Your contribution will be appreciated.

# License
This project is licensed under [BSD License](LICENSE).