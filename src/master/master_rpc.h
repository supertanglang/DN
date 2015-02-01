// Copyright (c) 2015 Chaobin Zhang. All rights reserved.
// Use of this source code is governed by the BSD license that can be
// found in the LICENSE file.

#ifndef  MASTER_MASTER_RPC_H_
#define  MASTER_MASTER_RPC_H_

#include <string>
#include <queue>

#include "base/macros.h"
#include "base/memory/ref_counted.h"
#include "base/memory/scoped_ptr.h"
#include "rpc/rpc_socket_server.h"
#include "thread/ninja_thread_delegate.h"

namespace master {

class MasterRPC
    : public NinjaThreadDelegate,
      public base::RefCountedThreadSafe<MasterRPC>,
      public rpc::RpcSocketServer::Observer {
 public:
  MasterRPC(const std::string& bind_ip, uint16 port);

  // NinjaThreadDelegate implementations.
  void Init() override;
  void InitAsync() override;
  void CleanUp() override;

  // rpc::RpcSocketServer::Observer implementations.
  void OnConnect(rpc::RpcConnection* connection) override;

 private:
  friend class base::RefCountedThreadSafe<MasterRPC>;
  virtual ~MasterRPC();

  std::string bind_ip_;
  uint16 port_;
  scoped_ptr<rpc::RpcSocketServer> rpc_socket_server_;

  DISALLOW_COPY_AND_ASSIGN(MasterRPC);
};

}  // namespace master

#endif  // MASTER_MASTER_RPC_H_