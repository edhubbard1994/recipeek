<h1>RECIPEEK</h1>

<h3>What is Recipeek?</h3>

This application aims to collect data on recipes from all across the internet and make them searchable in one open source place. This we hope can lay the groundwork for interesting datamining applications... its also the final project for our advanced algorithms class so please don't judge our "semester project" quality code.

<h3>Setup</h3>
<li>Pull source
<li>Download Docker Desktop at https://docker.com/
<li>Open terminal and go to repository directory

<h3>Build</h3>
<li>At the top level run "docker-compose build"

<h3>Running</h3>
<li>At the top level run "docker-compose up"

<h3>developing</h3>
<li>Make and save all code changes
<li>if changes in Django app, ensure all new imports (any pip installed package) are placed in requirements.txt
<li>EITHER run "docker-compose build" AND "docker-compose up"
<li>OR run "docker-compose up --build"
