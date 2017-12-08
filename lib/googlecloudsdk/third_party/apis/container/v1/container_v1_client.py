"""Generated client library for container version v1."""
# NOTE: This file is autogenerated and should not be edited by hand.
from apitools.base.py import base_api
from googlecloudsdk.third_party.apis.container.v1 import container_v1_messages as messages


class ContainerV1(base_api.BaseApiClient):
  """Generated client library for service container version v1."""

  MESSAGES_MODULE = messages
  BASE_URL = u'https://container.googleapis.com/'

  _PACKAGE = u'container'
  _SCOPES = [u'https://www.googleapis.com/auth/cloud-platform', u'https://www.googleapis.com/auth/userinfo.email']
  _VERSION = u'v1'
  _CLIENT_ID = '1042881264118.apps.googleusercontent.com'
  _CLIENT_SECRET = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _USER_AGENT = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _CLIENT_CLASS_NAME = u'ContainerV1'
  _URL_VERSION = u'v1'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None):
    """Create a new container handle."""
    url = url or self.BASE_URL
    super(ContainerV1, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers)
    self.masterProjects_zones_signedUrls = self.MasterProjectsZonesSignedUrlsService(self)
    self.masterProjects_zones_tokens = self.MasterProjectsZonesTokensService(self)
    self.masterProjects_zones = self.MasterProjectsZonesService(self)
    self.masterProjects = self.MasterProjectsService(self)
    self.projects_zones_clusters_nodePools = self.ProjectsZonesClustersNodePoolsService(self)
    self.projects_zones_clusters = self.ProjectsZonesClustersService(self)
    self.projects_zones_operations = self.ProjectsZonesOperationsService(self)
    self.projects_zones = self.ProjectsZonesService(self)
    self.projects = self.ProjectsService(self)

  class MasterProjectsZonesSignedUrlsService(base_api.BaseApiService):
    """Service class for the masterProjects_zones_signedUrls resource."""

    _NAME = u'masterProjects_zones_signedUrls'

    def __init__(self, client):
      super(ContainerV1.MasterProjectsZonesSignedUrlsService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      """Creates signed URLs that allow for writing a file to a private GCS bucket.
for storing backups of hosted master data. Signed URLs are explained here:
https://cloud.google.com/storage/docs/access-control#Signed-URLs

      Args:
        request: (ContainerMasterProjectsZonesSignedUrlsCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (SignedUrls) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'container.masterProjects.zones.signedUrls.create',
        ordered_params=[u'masterProjectId', u'zone'],
        path_params=[u'masterProjectId', u'zone'],
        query_params=[],
        relative_path=u'v1/masterProjects/{masterProjectId}/zones/{zone}/signedUrls',
        request_field=u'createSignedUrlsRequest',
        request_type_name=u'ContainerMasterProjectsZonesSignedUrlsCreateRequest',
        response_type_name=u'SignedUrls',
        supports_download=False,
    )

  class MasterProjectsZonesTokensService(base_api.BaseApiService):
    """Service class for the masterProjects_zones_tokens resource."""

    _NAME = u'masterProjects_zones_tokens'

    def __init__(self, client):
      super(ContainerV1.MasterProjectsZonesTokensService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      """Creates a compute-read-write (https://www.googleapis.com/auth/compute).
scoped OAuth2 access token for <project_number>, to allow a hosted master
to make modifications to its user's project.

      Args:
        request: (ContainerMasterProjectsZonesTokensCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Token) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'container.masterProjects.zones.tokens.create',
        ordered_params=[u'masterProjectId', u'zone'],
        path_params=[u'masterProjectId', u'zone'],
        query_params=[],
        relative_path=u'v1/masterProjects/{masterProjectId}/zones/{zone}/tokens',
        request_field=u'createTokenRequest',
        request_type_name=u'ContainerMasterProjectsZonesTokensCreateRequest',
        response_type_name=u'Token',
        supports_download=False,
    )

  class MasterProjectsZonesService(base_api.BaseApiService):
    """Service class for the masterProjects_zones resource."""

    _NAME = u'masterProjects_zones'

    def __init__(self, client):
      super(ContainerV1.MasterProjectsZonesService, self).__init__(client)
      self._upload_configs = {
          }

    def Authenticate(self, request, global_params=None):
      """Processes a request to authenticate a token. If it is able to authenticate.
the token, the email for the authorized user is also returned.
AuthenticateResponse also contains fields from the AuthenticateRequest. The
server is expected to only fill in the AuthenticateResponse.Status. This is
due to how the Authentication types are defined for the Kubernetes webhook
authenticator:
https://github.com/kubernetes/kubernetes/blob/master/pkg/apis/authentication.k8s.io/v1beta1/types.go.

      Args:
        request: (ContainerMasterProjectsZonesAuthenticateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (AuthenticateResponse) The response message.
      """
      config = self.GetMethodConfig('Authenticate')
      return self._RunMethod(
          config, request, global_params=global_params)

    Authenticate.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'container.masterProjects.zones.authenticate',
        ordered_params=[u'masterProjectId', u'zone', u'projectNumber', u'clusterId'],
        path_params=[u'clusterId', u'masterProjectId', u'projectNumber', u'zone'],
        query_params=[],
        relative_path=u'v1/masterProjects/{masterProjectId}/zones/{zone}/{projectNumber}/{clusterId}/authenticate',
        request_field=u'authenticateRequest',
        request_type_name=u'ContainerMasterProjectsZonesAuthenticateRequest',
        response_type_name=u'AuthenticateResponse',
        supports_download=False,
    )

    def Authorize(self, request, global_params=None):
      """Processes the attributes of a user request and determines whether or not.
to authorize the request. If unauthorized, a reason is also provided. The
AuthorizeResponse also contains fields from the AuthorizeRequest. The
server is expected to only fill in the AuthorizeResponse.Status. This is
due to how the Authorization types are defined for the Kubernetes webhook
authorizer:
https://github.com/kubernetes/kubernetes/blob/master/pkg/apis/authorization/v1beta1/types.go.

      Args:
        request: (ContainerMasterProjectsZonesAuthorizeRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (AuthorizeResponse) The response message.
      """
      config = self.GetMethodConfig('Authorize')
      return self._RunMethod(
          config, request, global_params=global_params)

    Authorize.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'container.masterProjects.zones.authorize',
        ordered_params=[u'masterProjectId', u'zone', u'projectNumber', u'clusterId'],
        path_params=[u'clusterId', u'masterProjectId', u'projectNumber', u'zone'],
        query_params=[],
        relative_path=u'v1/masterProjects/{masterProjectId}/zones/{zone}/{projectNumber}/{clusterId}/authorize',
        request_field=u'authorizeRequest',
        request_type_name=u'ContainerMasterProjectsZonesAuthorizeRequest',
        response_type_name=u'AuthorizeResponse',
        supports_download=False,
    )

  class MasterProjectsService(base_api.BaseApiService):
    """Service class for the masterProjects resource."""

    _NAME = u'masterProjects'

    def __init__(self, client):
      super(ContainerV1.MasterProjectsService, self).__init__(client)
      self._upload_configs = {
          }

  class ProjectsZonesClustersNodePoolsService(base_api.BaseApiService):
    """Service class for the projects_zones_clusters_nodePools resource."""

    _NAME = u'projects_zones_clusters_nodePools'

    def __init__(self, client):
      super(ContainerV1.ProjectsZonesClustersNodePoolsService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      """Creates a node pool for a cluster.

      Args:
        request: (ContainerProjectsZonesClustersNodePoolsCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'container.projects.zones.clusters.nodePools.create',
        ordered_params=[u'projectId', u'zone', u'clusterId'],
        path_params=[u'clusterId', u'projectId', u'zone'],
        query_params=[],
        relative_path=u'v1/projects/{projectId}/zones/{zone}/clusters/{clusterId}/nodePools',
        request_field=u'createNodePoolRequest',
        request_type_name=u'ContainerProjectsZonesClustersNodePoolsCreateRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      """Deletes a node pool from a cluster.

      Args:
        request: (ContainerProjectsZonesClustersNodePoolsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'DELETE',
        method_id=u'container.projects.zones.clusters.nodePools.delete',
        ordered_params=[u'projectId', u'zone', u'clusterId', u'nodePoolId'],
        path_params=[u'clusterId', u'nodePoolId', u'projectId', u'zone'],
        query_params=[],
        relative_path=u'v1/projects/{projectId}/zones/{zone}/clusters/{clusterId}/nodePools/{nodePoolId}',
        request_field='',
        request_type_name=u'ContainerProjectsZonesClustersNodePoolsDeleteRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      """Retrieves the node pool requested.

      Args:
        request: (ContainerProjectsZonesClustersNodePoolsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (NodePool) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'container.projects.zones.clusters.nodePools.get',
        ordered_params=[u'projectId', u'zone', u'clusterId', u'nodePoolId'],
        path_params=[u'clusterId', u'nodePoolId', u'projectId', u'zone'],
        query_params=[],
        relative_path=u'v1/projects/{projectId}/zones/{zone}/clusters/{clusterId}/nodePools/{nodePoolId}',
        request_field='',
        request_type_name=u'ContainerProjectsZonesClustersNodePoolsGetRequest',
        response_type_name=u'NodePool',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      """Lists the node pools for a cluster.

      Args:
        request: (ContainerProjectsZonesClustersNodePoolsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListNodePoolsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'container.projects.zones.clusters.nodePools.list',
        ordered_params=[u'projectId', u'zone', u'clusterId'],
        path_params=[u'clusterId', u'projectId', u'zone'],
        query_params=[],
        relative_path=u'v1/projects/{projectId}/zones/{zone}/clusters/{clusterId}/nodePools',
        request_field='',
        request_type_name=u'ContainerProjectsZonesClustersNodePoolsListRequest',
        response_type_name=u'ListNodePoolsResponse',
        supports_download=False,
    )

  class ProjectsZonesClustersService(base_api.BaseApiService):
    """Service class for the projects_zones_clusters resource."""

    _NAME = u'projects_zones_clusters'

    def __init__(self, client):
      super(ContainerV1.ProjectsZonesClustersService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      """Creates a cluster, consisting of the specified number and type of Google.
Compute Engine instances.

By default, the cluster is created in the project's
[default network](/compute/docs/networks-and-firewalls#networks).

One firewall is added for the cluster. After cluster creation,
the cluster creates routes for each node to allow the containers
on that node to communicate with all other instances in the
cluster.

Finally, an entry is added to the project's global metadata indicating
which CIDR range is being used by the cluster.

      Args:
        request: (ContainerProjectsZonesClustersCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'container.projects.zones.clusters.create',
        ordered_params=[u'projectId', u'zone'],
        path_params=[u'projectId', u'zone'],
        query_params=[],
        relative_path=u'v1/projects/{projectId}/zones/{zone}/clusters',
        request_field=u'createClusterRequest',
        request_type_name=u'ContainerProjectsZonesClustersCreateRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      """Deletes the cluster, including the Kubernetes endpoint and all worker.
nodes.

Firewalls and routes that were configured during cluster creation
are also deleted.

Other Google Compute Engine resources that might be in use by the cluster
(e.g. load balancer resources) will not be deleted if they weren't present
at the initial create time.

      Args:
        request: (ContainerProjectsZonesClustersDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'DELETE',
        method_id=u'container.projects.zones.clusters.delete',
        ordered_params=[u'projectId', u'zone', u'clusterId'],
        path_params=[u'clusterId', u'projectId', u'zone'],
        query_params=[],
        relative_path=u'v1/projects/{projectId}/zones/{zone}/clusters/{clusterId}',
        request_field='',
        request_type_name=u'ContainerProjectsZonesClustersDeleteRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      """Gets the details of a specific cluster.

      Args:
        request: (ContainerProjectsZonesClustersGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Cluster) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'container.projects.zones.clusters.get',
        ordered_params=[u'projectId', u'zone', u'clusterId'],
        path_params=[u'clusterId', u'projectId', u'zone'],
        query_params=[],
        relative_path=u'v1/projects/{projectId}/zones/{zone}/clusters/{clusterId}',
        request_field='',
        request_type_name=u'ContainerProjectsZonesClustersGetRequest',
        response_type_name=u'Cluster',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      """Lists all clusters owned by a project in either the specified zone or all.
zones.

      Args:
        request: (ContainerProjectsZonesClustersListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListClustersResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'container.projects.zones.clusters.list',
        ordered_params=[u'projectId', u'zone'],
        path_params=[u'projectId', u'zone'],
        query_params=[],
        relative_path=u'v1/projects/{projectId}/zones/{zone}/clusters',
        request_field='',
        request_type_name=u'ContainerProjectsZonesClustersListRequest',
        response_type_name=u'ListClustersResponse',
        supports_download=False,
    )

    def Update(self, request, global_params=None):
      """Updates the settings of a specific cluster.

      Args:
        request: (ContainerProjectsZonesClustersUpdateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Update')
      return self._RunMethod(
          config, request, global_params=global_params)

    Update.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'PUT',
        method_id=u'container.projects.zones.clusters.update',
        ordered_params=[u'projectId', u'zone', u'clusterId'],
        path_params=[u'clusterId', u'projectId', u'zone'],
        query_params=[],
        relative_path=u'v1/projects/{projectId}/zones/{zone}/clusters/{clusterId}',
        request_field=u'updateClusterRequest',
        request_type_name=u'ContainerProjectsZonesClustersUpdateRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

  class ProjectsZonesOperationsService(base_api.BaseApiService):
    """Service class for the projects_zones_operations resource."""

    _NAME = u'projects_zones_operations'

    def __init__(self, client):
      super(ContainerV1.ProjectsZonesOperationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      """Gets the specified operation.

      Args:
        request: (ContainerProjectsZonesOperationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'container.projects.zones.operations.get',
        ordered_params=[u'projectId', u'zone', u'operationId'],
        path_params=[u'operationId', u'projectId', u'zone'],
        query_params=[],
        relative_path=u'v1/projects/{projectId}/zones/{zone}/operations/{operationId}',
        request_field='',
        request_type_name=u'ContainerProjectsZonesOperationsGetRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      """Lists all operations in a project in a specific zone or all zones.

      Args:
        request: (ContainerProjectsZonesOperationsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListOperationsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'container.projects.zones.operations.list',
        ordered_params=[u'projectId', u'zone'],
        path_params=[u'projectId', u'zone'],
        query_params=[],
        relative_path=u'v1/projects/{projectId}/zones/{zone}/operations',
        request_field='',
        request_type_name=u'ContainerProjectsZonesOperationsListRequest',
        response_type_name=u'ListOperationsResponse',
        supports_download=False,
    )

  class ProjectsZonesService(base_api.BaseApiService):
    """Service class for the projects_zones resource."""

    _NAME = u'projects_zones'

    def __init__(self, client):
      super(ContainerV1.ProjectsZonesService, self).__init__(client)
      self._upload_configs = {
          }

    def GetServerconfig(self, request, global_params=None):
      """Returns configuration info about the Container Engine service.

      Args:
        request: (ContainerProjectsZonesGetServerconfigRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ServerConfig) The response message.
      """
      config = self.GetMethodConfig('GetServerconfig')
      return self._RunMethod(
          config, request, global_params=global_params)

    GetServerconfig.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'container.projects.zones.getServerconfig',
        ordered_params=[u'projectId', u'zone'],
        path_params=[u'projectId', u'zone'],
        query_params=[],
        relative_path=u'v1/projects/{projectId}/zones/{zone}/serverconfig',
        request_field='',
        request_type_name=u'ContainerProjectsZonesGetServerconfigRequest',
        response_type_name=u'ServerConfig',
        supports_download=False,
    )

  class ProjectsService(base_api.BaseApiService):
    """Service class for the projects resource."""

    _NAME = u'projects'

    def __init__(self, client):
      super(ContainerV1.ProjectsService, self).__init__(client)
      self._upload_configs = {
          }
