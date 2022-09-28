exports.handler = async (event) => {
    // TODO implement
    const botResponse =  [{
        'type': 'unstructured',
        'unstructured': {
          'text': "Application under development. Search functionality will be implemented in Assignment 2"
        }
    }]
      
    return {
        'statusCode': 200,
        'messages': botResponse
    }
};
