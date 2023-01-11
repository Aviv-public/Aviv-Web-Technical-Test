FROM mcr.microsoft.com/dotnet/aspnet:6.0-alpine AS base
WORKDIR /home/pricemap/app

FROM mcr.microsoft.com/dotnet/sdk:6.0-alpine AS build
WORKDIR /home/pricemap/src
COPY [".", "."]
COPY ["nuget.config", "."]

RUN dotnet restore "pricemap.csproj"
COPY . .
WORKDIR "/home/pricemap/src"
RUN dotnet build "pricemap.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "pricemap.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /home/pricemap/app
COPY --from=publish /app/publish .
# Adding permisisons
RUN chown -R $USER:$USER /app && chmod -R 777 /app

RUN apk update && apk add --no-cache busybox-extras 

RUN apk add --no-cache curl

RUN apk add --no-cache tcptraceroute

# switch user
USER $USER
EXPOSE 8080
ENTRYPOINT ["dotnet", "pricemap.dll"]
