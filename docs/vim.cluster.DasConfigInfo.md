vim.cluster.DasConfigInfo
=========================
inherits from [vmodl.DynamicData](docs/vmodl.DynamicData.md)


The <a href="vim.cluster.DasConfigInfo.md">ClusterDasConfigInfo</a> data object contains configuration data   about the HA service on a cluster.   <p>   All fields are optional. If you set the <code>modify</code>   parameter to <code>true</code> when you call   <a href="vim.ComputeResource.md#reconfigureEx">ReconfigureComputeResource_Task</a>, an unset property has no effect   on the existing property value in the cluster configuration on the Server.   If you set the <code>modify</code> parameter to <code>false</code> when you   reconfigure a cluster, the cluster configuration is reverted to the default   values, then the new configuration values are applied.

| property | type | optional | priv | desc |
|:---------|:-----|:---------|:-----|:-----|
| enabled | bool | true | None | Flag to indicate whether or not vSphere HA feature is enabled. |
| vmMonitoring | string | true | None | Level of HA Virtual Machine Health Monitoring Service.   You can monitor both guest and application heartbeats, guest heartbeats only,   or you can disable the service. See <a href="vim.cluster.DasConfigInfo.VmMonitoringState.md">ClusterDasConfigInfoVmMonitoringState</a>.   The default value is <a href="vim.cluster.DasConfigInfo.VmMonitoringState.md#vmMonitoringDisabled">vmMonitoringDisabled</a>.  <p>  The Service level specified for the cluster determines  the possible monitoring settings that you can use for individual virtual machines.  See <a href="vim.cluster.VmToolsMonitoringSettings.md">ClusterVmToolsMonitoringSettings</a>.<a href="vim.cluster.VmToolsMonitoringSettings.md#vmMonitoring">vmMonitoring</a>. |
| hostMonitoring | string | true | None | Determines whether HA restarts virtual machines after a host fails.   The default value is   <a href="vim.cluster.DasConfigInfo.ServiceState.md">ClusterDasConfigInfoServiceState</a>.<a href="vim.cluster.DasConfigInfo.ServiceState.md#enabled">enabled</a>.   This property is meaningful only when   <a href="vim.cluster.DasConfigInfo.md">ClusterDasConfigInfo</a>.<a href="vim.cluster.DasConfigInfo.md#enabled">enabled</a> is <code>true</code>.   <p>   When <code>hostMonitoring</code> is   <a href="vim.cluster.DasConfigInfo.ServiceState.md#enabled">enabled</a>, HA restarts virtual machines   after a host fails.   <p>   When <code>hostMonitoring</code> is   <a href="vim.cluster.DasConfigInfo.ServiceState.md#disabled">disabled</a>, HA does not restart   virtual machines after a host fails.   The status of Host Monitoring does not affect other services such   as virtual machine Health Monitoring or Fault Tolerance.   The rest of the cluster operations follow normal processing.   No configuration information is lost and re-enabling the service   is a quick operation. |
| failoverLevel | int | true | None | Configured failover level. This is the number of physical host failures   that can be tolerated without impacting the ability to satisfy the   minimums for all running virtual machines. Acceptable values range from one to    four. |
| admissionControlPolicy | [vim.cluster.DasAdmissionControlPolicy](vim.cluster.DasAdmissionControlPolicy.md "vim.cluster.DasAdmissionControlPolicy") | true | None | Virtual machine admission control policy for vSphere HA.  The policies specify resource availability for failover support.  <ul>  <li>Failover host admission policy      <a href="vim.cluster.FailoverHostAdmissionControlPolicy.md">ClusterFailoverHostAdmissionControlPolicy</a> -      currently you can specify only one failover host.</li>  <li>Failover level policy      <a href="vim.cluster.FailoverLevelAdmissionControlPolicy.md">ClusterFailoverLevelAdmissionControlPolicy</a> -      the limit of host failures for which resources are reserved.      When you use the failover level policy,      HA partitions resources into slots. A slot represents the minimum      CPU and memory resources that are required to support      any powered on virtual machine in the cluster.      To retrieve information about partitioned resources, use the      <a href="vim.ClusterComputeResource.md#retrieveDasAdvancedRuntimeInfo">RetrieveDasAdvancedRuntimeInfo</a>      method. </li>  <li>Resources admission policy      <a href="vim.cluster.FailoverResourcesAdmissionControlPolicy.md">ClusterFailoverResourcesAdmissionControlPolicy</a> -      CPU and memory resources reserved for failover support.      When you use the resources policy, you can reserve      a percentage of the aggregate cluster resource for failover.      </li>  </ul> |
| admissionControlEnabled | bool | true | None | Flag that determines whether strict admission control is enabled.   When you use admission control, the following operations are   prevented, if doing so would violate the <a href="vim.cluster.DasConfigInfo.md#admissionControlPolicy">admissionControlPolicy</a>.   <ul>   <li>Powering on a virtual machine in the cluster.</li>   <li>Migrating a virtual machine into the cluster.</li>   <li>Increasing the CPU or memory reservation of powered-on       virtual machines in the cluster.</li>   </ul>   <p>   With admission control disabled, there is no assurance that   all virtual machines in the HA cluster can be restarted after   a host failure. VMware recommends that you do not disable   admission control, but you might need to do so temporarily,   for the following reasons:   <ul>   <li>If you need to violate the failover constraints when there       are not enough resources to support them (for example,       if you are placing hosts in standby mode to test them       for use with DPM).   </li>   <li>If an automated process needs to take actions that might       temporarily violate the failover constraints (for example,       as part of an upgrade directed by VMware Update Manager).   </li>   <li>If you need to perform testing or maintenance operations.</li>   </ul> |
| defaultVmSettings | [vim.cluster.DasVmSettings](vim.cluster.DasVmSettings.md "vim.cluster.DasVmSettings") | true | None | Cluster-wide defaults for virtual machine HA settings.   When a virtual machine has no HA configuration   (<a href="vim.cluster.DasVmConfigSpec.md">ClusterDasVmConfigSpec</a>), it uses the values   specified here. |
| option | [vim.option.OptionValue](vim.option.OptionValue.md "vim.option.OptionValue") | true | None | Advanced settings. |
| heartbeatDatastore | [vim.Datastore](vim.Datastore.md "vim.Datastore") | true | None | The list of preferred datastores to use for storage heartbeating.  Each of the specified datastores should be active and mounted  by more than one host. There is no limit on the number of specified  datastores and no priority among them.  The specified datastores will replace those previously specified and  an empty list will delete all such earlier specified ones.  <p>  vCenter Server chooses the heartbeat datastores for a host from the  set specified by <a href="vim.cluster.DasConfigInfo.md#hBDatastoreCandidatePolicy">hBDatastoreCandidatePolicy</a>.  The choice is made based on datastore connectivity and storage array  redundancy (in case of VMFS).  <p>  The final set of selected heartbeat datastores is reported via  <a href="vim.cluster.DasAdvancedRuntimeInfo.md#heartbeatDatastoreInfo">heartbeatDatastoreInfo</a>. |
| hBDatastoreCandidatePolicy | string | true | None | The policy on what datastores will be used by vCenter Server to choose  heartbeat datastores.  See <a href="vim.cluster.DasConfigInfo.HBDatastoreCandidate.md">ClusterDasConfigInfoHBDatastoreCandidate</a> for all options.  The default value is  <a href="vim.cluster.DasConfigInfo.HBDatastoreCandidate.md#allFeasibleDsWithUserPreference">allFeasibleDsWithUserPreference</a>. |

