# TasksApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**controllerTasksControllerCreate**](TasksApi.md#controllerTasksControllerCreate) | **POST** /board/{board_id}/tasks | Create a new task
[**controllerTasksControllerDelete**](TasksApi.md#controllerTasksControllerDelete) | **DELETE** /tasks/{id} | Delete a task
[**controllerTasksControllerReadTasks**](TasksApi.md#controllerTasksControllerReadTasks) | **GET** /board/{board_id}/tasks | Read all tasks
[**controllerTasksControllerUpdate**](TasksApi.md#controllerTasksControllerUpdate) | **PUT** /tasks/{id} | Update a task


<a name="controllerTasksControllerCreate"></a>
# **controllerTasksControllerCreate**
> controllerTasksControllerCreate(boardId, task)

Create a new task

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TasksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost/api");

    TasksApi apiInstance = new TasksApi(defaultClient);
    String boardId = "boardId_example"; // String | The ID of the board to get
    Task task = new Task(); // Task | Task to create
    try {
      apiInstance.controllerTasksControllerCreate(boardId, task);
    } catch (ApiException e) {
      System.err.println("Exception when calling TasksApi#controllerTasksControllerCreate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **boardId** | **String**| The ID of the board to get |
 **task** | [**Task**](Task.md)| Task to create |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully created a new task |  -  |

<a name="controllerTasksControllerDelete"></a>
# **controllerTasksControllerDelete**
> controllerTasksControllerDelete(id)

Delete a task

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TasksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost/api");

    TasksApi apiInstance = new TasksApi(defaultClient);
    String id = "id_example"; // String | The ID of the task to get
    try {
      apiInstance.controllerTasksControllerDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling TasksApi#controllerTasksControllerDelete");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| The ID of the task to get |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successfully deleted task |  -  |

<a name="controllerTasksControllerReadTasks"></a>
# **controllerTasksControllerReadTasks**
> controllerTasksControllerReadTasks(boardId)

Read all tasks

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TasksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost/api");

    TasksApi apiInstance = new TasksApi(defaultClient);
    String boardId = "boardId_example"; // String | The ID of the board to get
    try {
      apiInstance.controllerTasksControllerReadTasks(boardId);
    } catch (ApiException e) {
      System.err.println("Exception when calling TasksApi#controllerTasksControllerReadTasks");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **boardId** | **String**| The ID of the board to get |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully read all tasks |  -  |

<a name="controllerTasksControllerUpdate"></a>
# **controllerTasksControllerUpdate**
> controllerTasksControllerUpdate(id, body)

Update a task

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TasksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost/api");

    TasksApi apiInstance = new TasksApi(defaultClient);
    String id = "id_example"; // String | The ID of the task to get
    Object body = null; // Object | 
    try {
      apiInstance.controllerTasksControllerUpdate(id, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling TasksApi#controllerTasksControllerUpdate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| The ID of the task to get |
 **body** | **Object**|  | [optional]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated task |  -  |

