# File Structure

## Integrated

```
📦Homies
 ┣ 📂app
 ┃ ┣ 📂internal
 ┃ ┃ ┣ 📂finance
 ┃ ┃ ┣ 📂home
 ┃ ┃ ┣ 📂hospital_core
 ┃ ┃ ┣ 📂human_resource
 ┃ ┃ ┣ 📂logistics
 ┃ ┃ ┗ 📜app.py
 ┃ ┗ 📂public
 ┃ ┃ ┣ 📂doctors
 ┃ ┃ ┣ 📂careers
 ┃ ┃ ┣ 📂home
 ┃ ┃ ┃ ┣ 📂routers
 ┃ ┃ ┃ ┃ ┣ 📂api
 ┃ ┃ ┃ ┃ ┗ 📂web
 ┃ ┃ ┃ ┃ ┃ ┗ 📜homeRoute.py
 ┃ ┃ ┃ ┗ 📂views
 ┃ ┃ ┃ ┃ ┣ 📂content
 ┃ ┃ ┃ ┃ ┃ ┣ 📜home.html
 ┃ ┃ ┃ ┃ ┃ ┗ 📜login.html
 ┃ ┃ ┃ ┃ ┗ 📂templates
 ┃ ┃ ┃ ┃ ┃ ┗ 📂public
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📂components
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜footer_section.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜topbar.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜footer.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┣ 📜header.html
 ┃ ┃ ┃ ┃ ┃ ┃ ┗ 📜layout.html
 ┃ ┃ ┣ 📂visitors
 ┃ ┃ ┗ 📜app.py
 ┣ 📂static
 ┃ ┣ 📂dist
 ┃ ┣ 📂src
 ┃ ┃ ┣ 📂css
 ┃ ┃ ┣ 📂files
 ┃ ┃ ┣ 📂img
 ┃ ┃ ┗ 📂js
 ┃ ┗ 📂plugins
 ┣ 📜.gitattributes
 ┣ 📜.gitignore
 ┣ 📜database.py
 ┣ 📜file_structure.md
 ┣ 📜hashing.py
 ┣ 📜jwt_token.py
 ┣ 📜main.py
 ┣ 📜models.py
 ┣ 📜oauth2.py
 ┗ 📜requirements.txt
 ```

## Per Subsystem

For specific folders: `/app/internal`, `/static/src/{css|js|img|files}/{internal|public}`

```
📦Specific Folder
 ┣ 📂core
 ┃ ┣ 📂{abbr. subsystem}
 ┃ ┣ 📂{abbr. subsystem}
 ┃ ┣ 📂{abbr. subsystem}
 ┃ ┣ 📂{abbr. subsystem}
 ┣ 📂finance
 ┃ ┣ 📂{abbr. subsystem}
 ┃ ┣ 📂{abbr. subsystem}
 ┃ ┣ 📂{abbr. subsystem}
 ┃ ┣ 📂{abbr. subsystem}
 ┣ 📂human_resouce
 ┃ ┣ 📂{abbr. subsystem}
 ┃ ┣ 📂{abbr. subsystem}
 ┃ ┣ 📂{abbr. subsystem}
 ┃ ┣ 📂{abbr. subsystem}
 ┗ 📂logistics
   ┣ 📂{abbr. subsystem}
   ┣ 📂{abbr. subsystem}
   ┣ 📂{abbr. subsystem}
   ┗ 📂{abbr. subsystem}

```