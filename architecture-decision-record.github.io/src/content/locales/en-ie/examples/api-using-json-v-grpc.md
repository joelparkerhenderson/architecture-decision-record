# Architecture Decision Record: API using JSON v. gRPC

## Status

Accepted

## Context

We are designing an API for a new service that will be used by multiple clients. We have been considering two options for implementing the API: using JSON over HTTP or using gRPC.

JSON over HTTP is a widely-used approach for building APIs, and it is supported by many programming languages and frameworks. This approach is simple, lightweight, and easy to understand, making it a good choice for many projects. However, it can be less efficient than other options, especially when it comes to handling large amounts of data.

gRPC, on the other hand, is a newer technology that offers a more efficient way of building APIs. It uses binary serialization to transfer data, which can be faster and more compact than using JSON. gRPC also supports bidirectional streaming, making it a good choice for real-time applications.

## Decision

After considering the pros and cons of both options, we have decided to use gRPC for our API. Although JSON over HTTP is a simpler option, we believe that gRPC will provide a more efficient and scalable solution for our service. We also anticipate that our API will handle a large amount of data, and gRPC's binary serialization will be more efficient for this use case.

In addition, we believe that gRPC's support for bidirectional streaming will be beneficial for real-time applications that we may develop in the future.

## Consequences

By choosing gRPC, we will need to use a different set of tools and libraries to build our API compared to using JSON over HTTP. This may require additional time and effort to learn and implement these technologies. Additionally, clients who want to use our API will need to use gRPC-compatible libraries, which may not be as widely supported as JSON over HTTP libraries.

However, we believe that the benefits of using gRPC outweigh these potential drawbacks, and we are confident that this decision will result in a more efficient and scalable API.