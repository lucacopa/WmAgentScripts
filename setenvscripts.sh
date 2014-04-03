USER=$(whoami)
kinit $USER@CERN.CH
source /afs/cern.ch/project/gd/LCG-share/3.2.11-1/etc/profile.d/grid-env.sh
{
source /data/srv/wmagent/current/apps/wmagent/etc/profile.d/init.sh
} || {
echo ‘This machine does not have WMAgent installed. Not sourcing Agent environment’
}
{
git pull
} || {
echo ‘This machine does not have git installed. Not updating WmAgentScripts repository’
}
voms-proxy-init -voms cms