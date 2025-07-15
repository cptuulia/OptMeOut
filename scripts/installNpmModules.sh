

echo make templates
../dockerRunBuildTemplates.sh 
cd dist
echo build npm modules
rm -rf node_modules 
npm install
cd ..