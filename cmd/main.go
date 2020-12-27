package main

import (
	"log"
	"net"

	"google.golang.org/grpc"

	"grpc_demo/internal/grpc/protobuf"
)

const (
	port = ":8787"
)

func main() {
	// Create gRPC Server
	lis, err := net.Listen("tcp", port)
	if err != nil {
		log.Fatalf("failed to listen: %v", err)
	}
	s := grpc.NewServer()
	log.Println("gRPC server is running.")

	protobuf.RegisterTesterServer(s, &protobuf.Server{})
	if err := s.Serve(lis); err != nil {
		log.Fatalf("failed to serve: %v", err)
	}
}
