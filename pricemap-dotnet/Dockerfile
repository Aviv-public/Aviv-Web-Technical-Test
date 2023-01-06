FROM 936992537267.dkr.ecr.eu-west-1.amazonaws.com/groupeseloger/sl.alpine-core6.0-runtime:latest AS base
WORKDIR /app

FROM 936992537267.dkr.ecr.eu-west-1.amazonaws.com/groupeseloger/sl.alpine-core6.0-build:latest AS build
WORKDIR /src
COPY [".", "."]
COPY ["nuget.config", "."]

RUN dotnet restore "pricemap.csproj"
COPY . .
WORKDIR "/src"
RUN dotnet build "pricemap.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "pricemap.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
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
