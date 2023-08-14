# BoardApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**controllerBoardControllerReadBoard**](BoardApi.md#controllerBoardControllerReadBoard) | **GET** /board | Read the board configuration


<a name="controllerBoardControllerReadBoard"></a>
# **controllerBoardControllerReadBoard**
> controllerBoardControllerReadBoard(boardId)

Read the board configuration

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BoardApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost/api");

    BoardApi apiInstance = new BoardApi(defaultClient);
    String boardId = "boardId_example"; // String | The ID of the board to get
    try {
      apiInstance.controllerBoardControllerReadBoard(boardId);
    } catch (ApiException e) {
      System.err.println("Exception when calling BoardApi#controllerBoardControllerReadBoard");
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
**200** | Successfully read the board configuration |  -  |

