class ProviderNotFoundError(Exception):
    ...

class ProviderNotWorkingError(Exception):
    ...

class StreamNotSupportedError(Exception):
    ...

class ModelNotFoundError(Exception):
    ...

class ModelNotAllowedError(Exception):
    ...

class RetryProviderError(Exception):
    ...

class RetryNoProviderError(Exception):
    ...

class VersionNotFoundError(Exception):
    ...

class NestAsyncioError(Exception):
    ...

class ModelNotSupportedError(Exception):
    ...

class MissingRequirementsError(Exception):
    ...

class MissingAuthError(Exception):
    ...

class NoImageResponseError(Exception):
    ...

class RateLimitError(Exception):
    ...